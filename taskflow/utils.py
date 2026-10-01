"""Utility functions for TaskFlow"""

from datetime import datetime, timedelta
from typing import List
from .models import Task, Status


def format_task_display(task: Task) -> str:
    """Format task for display"""
    status_emoji = {
        Status.PENDING: "⏳",
        Status.IN_PROGRESS: "🔄",
        Status.COMPLETED: "✅",
        Status.ARCHIVED: "📦",
    }
    return (
        f"{status_emoji.get(task.status, '•')} [{task.priority.name}] "
        f"{task.title} (Due: {task.due_date.strftime('%Y-%m-%d') if task.due_date else 'N/A'})"
    )


def get_upcoming_deadline(tasks: List[Task], days: int = 7) -> List[Task]:
    """Get tasks with upcoming deadlines"""
    now = datetime.now()
    deadline = now + timedelta(days=days)
    return [
        t for t in tasks
        if t.due_date and now <= t.due_date <= deadline and t.status != Status.COMPLETED
    ]


def export_to_json(data: dict) -> str:
    """Export data to JSON format"""
    import json
    return json.dumps(data, indent=2, default=str)
