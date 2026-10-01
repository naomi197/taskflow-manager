"""Task management core functionality"""

from typing import List, Optional, Dict
from datetime import datetime
from .models import Task, Project, Priority, Status


class TaskManager:
    """Main task management system"""

    def __init__(self):
        """Initialize task manager"""
        self.projects: Dict[str, Project] = {}
        self.tasks: Dict[str, Task] = {}

    def create_project(self, name: str, description: str = "") -> Project:
        """Create a new project"""
        project = Project(name=name, description=description)
        self.projects[project.project_id] = project
        return project

    def get_project(self, project_id: str) -> Optional[Project]:
        """Get project by ID"""
        return self.projects.get(project_id)

    def delete_project(self, project_id: str) -> bool:
        """Delete project by ID"""
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

    def list_projects(self) -> List[Project]:
        """Get all projects"""
        return list(self.projects.values())

    def create_task(self, title: str, project_id: str, **kwargs) -> Optional[Task]:
        """Create task in project"""
        project = self.get_project(project_id)
        if not project:
            return None

        task = Task(title=title, **kwargs)
        self.tasks[task.task_id] = task
        project.add_task(task)
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """Get task by ID"""
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, **kwargs) -> bool:
        """Update task attributes"""
        task = self.get_task(task_id)
        if not task:
            return False

        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        task.updated_at = datetime.now()
        return True

    def delete_task(self, task_id: str, project_id: str) -> bool:
        """Delete task"""
        if task_id in self.tasks:
            del self.tasks[task_id]
            project = self.get_project(project_id)
            if project:
                project.remove_task(task_id)
            return True
        return False

    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """Get tasks filtered by priority"""
        return [t for t in self.tasks.values() if t.priority == priority]

    def get_tasks_by_status(self, status: Status) -> List[Task]:
        """Get tasks filtered by status"""
        return [t for t in self.tasks.values() if t.status == status]

    def get_overdue_tasks(self) -> List[Task]:
        """Get all overdue tasks"""
        now = datetime.now()
        return [
            t for t in self.tasks.values()
            if t.due_date and t.due_date < now and t.status != Status.COMPLETED
        ]

    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by title or description"""
        query_lower = query.lower()
        return [
            t for t in self.tasks.values()
            if query_lower in t.title.lower() or query_lower in t.description.lower()
        ]

    def get_statistics(self) -> Dict:
        """Get management statistics"""
        return {
            "total_projects": len(self.projects),
            "total_tasks": len(self.tasks),
            "completed_tasks": len(self.get_tasks_by_status(Status.COMPLETED)),
            "pending_tasks": len(self.get_tasks_by_status(Status.PENDING)),
            "in_progress_tasks": len(self.get_tasks_by_status(Status.IN_PROGRESS)),
            "overdue_tasks": len(self.get_overdue_tasks()),
        }
