"""Tests for TaskFlow manager"""

import unittest
from taskflow.manager import TaskManager
from taskflow.models import Priority, Status


class TestTaskManager(unittest.TestCase):
    """Test TaskManager functionality"""

    def setUp(self):
        self.manager = TaskManager()
        self.project = self.manager.create_project("Test Project")

    def test_create_project(self):
        """Test project creation"""
        self.assertIsNotNone(self.project)
        self.assertEqual(self.project.name, "Test Project")

    def test_create_task(self):
        """Test task creation"""
        task = self.manager.create_task(
            "Test Task",
            self.project.project_id,
            priority=Priority.HIGH,
        )
        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Test Task")

    def test_get_statistics(self):
        """Test statistics generation"""
        self.manager.create_task("Task 1", self.project.project_id)
        self.manager.create_task("Task 2", self.project.project_id)
        stats = self.manager.get_statistics()
        self.assertEqual(stats["total_projects"], 1)
        self.assertEqual(stats["total_tasks"], 2)

    def test_search_tasks(self):
        """Test task search functionality"""
        self.manager.create_task("Python Task", self.project.project_id)
        self.manager.create_task("Java Task", self.project.project_id)
        results = self.manager.search_tasks("Python")
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
