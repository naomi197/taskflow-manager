# TaskFlow Manager 📋

A professional, compact Python library for task and project management with advanced features.

## Features ✨

- **Project Management**: Create and manage multiple projects
- **Task Tracking**: Full task lifecycle management (pending → in progress → completed)
- **Priority Levels**: Support for LOW, MEDIUM, HIGH, and CRITICAL priorities
- **Advanced Filtering**: Search by status, priority, tags, and due dates
- **Overdue Detection**: Automatically identify overdue tasks
- **Statistics**: Get comprehensive project and task statistics
- **Data Export**: Easy serialization to JSON format

## Installation

```bash
pip install taskflow-manager
```

## Quick Start

```python
from taskflow import TaskManager, Priority, Status

# Initialize manager
manager = TaskManager()

# Create project
project = manager.create_project("My Project")

# Create task
task = manager.create_task(
    title="Implement feature",
    project_id=project.project_id,
    priority=Priority.HIGH,
    description="Build new authentication module"
)

# Update task
manager.update_task(task.task_id, status=Status.IN_PROGRESS)

# Get statistics
stats = manager.get_statistics()
print(stats)
```

## Core Classes

### TaskManager
Main manager for all operations.

**Key Methods:**
- `create_project(name, description)` - Create new project
- `create_task(title, project_id, **kwargs)` - Create new task
- `update_task(task_id, **kwargs)` - Update task
- `get_tasks_by_priority(priority)` - Filter by priority
- `get_tasks_by_status(status)` - Filter by status
- `get_overdue_tasks()` - Get all overdue tasks
- `search_tasks(query)` - Search by title/description
- `get_statistics()` - Get management statistics

### Task
Represents individual tasks.

**Attributes:**
- `title` - Task title
- `description` - Detailed description
- `priority` - Priority level (Priority enum)
- `status` - Current status (Status enum)
- `due_date` - Optional deadline
- `tags` - List of tags
- `task_id` - Unique identifier
- `created_at`, `updated_at` - Timestamps

### Project
Represents project containers.

**Attributes:**
- `name` - Project name
- `description` - Project description
- `tasks` - List of tasks
- `project_id` - Unique identifier

**Methods:**
- `add_task(task)` - Add task to project
- `remove_task(task_id)` - Remove task
- `get_progress()` - Get completion percentage

## Enums

### Priority
```python
from taskflow import Priority
Priority.LOW       # 1
Priority.MEDIUM    # 2
Priority.HIGH      # 3
Priority.CRITICAL  # 4
```

### Status
```python
from taskflow import Status
Status.PENDING      # "pending"
Status.IN_PROGRESS  # "in_progress"
Status.COMPLETED    # "completed"
Status.ARCHIVED     # "archived"
```

## Advanced Usage

### Filtering Tasks
```python
# Get high priority tasks
high_priority = manager.get_tasks_by_priority(Priority.HIGH)

# Get pending tasks
pending = manager.get_tasks_by_status(Status.PENDING)

# Get overdue tasks
overdue = manager.get_overdue_tasks()

# Search tasks
results = manager.search_tasks("authentication")
```

### Data Export
```python
project_data = project.to_dict()
task_data = task.to_dict()
```

## Testing

Run the test suite:

```bash
python -m pytest tests/
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
