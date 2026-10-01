"""Data models for TaskFlow library"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, List
import uuid


class Priority(Enum):
    """Task priority levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Status(Enum):
    """Task status states"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"


@dataclass
class Task:
    """Task data model"""
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    status: Status = Status.PENDING
    due_date: Optional[datetime] = None
    tags: List[str] = field(default_factory=list)
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def mark_complete(self) -> None:
        """Mark task as completed"""
        self.status = Status.COMPLETED
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Convert task to dictionary"""
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority.name,
            "status": self.status.value,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


@dataclass
class Project:
    """Project data model"""
    name: str
    description: str = ""
    tasks: List[Task] = field(default_factory=list)
    project_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def add_task(self, task: Task) -> None:
        """Add task to project"""
        self.tasks.append(task)
        self.updated_at = datetime.now()

    def remove_task(self, task_id: str) -> bool:
        """Remove task from project"""
        initial_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        if len(self.tasks) < initial_length:
            self.updated_at = datetime.now()
            return True
        return False

    def get_progress(self) -> float:
        """Get project completion percentage"""
        if not self.tasks:
            return 0.0
        completed = sum(1 for t in self.tasks if t.status == Status.COMPLETED)
        return (completed / len(self.tasks)) * 100

    def to_dict(self) -> dict:
        """Convert project to dictionary"""
        return {
            "id": self.project_id,
            "name": self.name,
            "description": self.description,
            "tasks_count": len(self.tasks),
            "progress": self.get_progress(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
