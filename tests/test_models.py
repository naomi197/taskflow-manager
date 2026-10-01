"""Tests for TaskFlow models"""

import unittest
from datetime import datetime, timedelta
from taskflow.models import Task, Project, Priority, Status


class TestTask(unittest.TestCase):
    """Test Task model"""

    def setUp(self):
        self.task = Task(
            title="Test Task",
            description="Test Description",
            priority=Priority.HIGH,
        )

    def test_task_creation(self):
        """Test task creation"""
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.status, Status.PENDING)
        self.assertEqual(self.task.priority, Priority.HIGH)

    def test_mark_complete(self):
        """Test marking task as complete"""
        self.task.mark_complete()
        self.assertEqual(self.task.status, Status.COMPLETED)

    def test_task_to_dict(self):
        """Test task serialization"""
        task_dict = self.task.to_dict()
        self.assertEqual(task_dict["title"], "Test Task")
        self.assertEqual(task_dict["status"], "completed" if self.task.status == Status.COMPLETED else "pending")


class TestProject(unittest.TestCase):
    """Test Project model"""

    def setUp(self):
        self.project = Project(name="Test Project")
        self.task = Task(title="Test Task")

    def test_project_creation(self):
        """Test project creation"""
        self.assertEqual(self.project.name, "Test Project")
        self.assertEqual(len(self.project.tasks), 0)

    def test_add_task(self):
        """Test adding task to project"""
        self.project.add_task(self.task)
        self.assertEqual(len(self.project.tasks), 1)

    def test_get_progress(self):
        """Test project progress calculation"""
        self.project.add_task(self.task)
        self.assertEqual(self.project.get_progress(), 0.0)
        self.task.mark_complete()
        self.assertEqual(self.project.get_progress(), 100.0)


if __name__ == "__main__":
    unittest.main()
