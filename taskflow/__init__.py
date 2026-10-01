"""TaskFlow - Professional Task Management Library"""

__version__ = "1.0.0"
__author__ = "TaskFlow Team"

from .manager import TaskManager
from .models import Task, Project, Priority, Status

__all__ = ["TaskManager", "Task", "Project", "Priority", "Status"]
