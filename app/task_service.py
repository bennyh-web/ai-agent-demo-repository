"""
Task management service.
Handles task creation, progress status, and labor estimates.
"""

from app.models import Task
from app.utils import validate_positive_amount, validate_positive_quantity, round_currency


def create_task(
    task_id: str,
    title: str,
    hourly_rate: float,
    estimated_hours: int
) -> Task:
    """Creates a new project task."""
    if not task_id.strip():
        raise ValueError("Task ID cannot be empty")
    if not title.strip():
        raise ValueError("Task title cannot be empty")
    validate_positive_amount(hourly_rate, "hourly_rate")
    validate_positive_quantity(estimated_hours, "estimated_hours")
    return Task(
        task_id=task_id,
        title=title,
        hourly_rate=hourly_rate,
        estimated_hours=estimated_hours
    )


def complete_task(task: Task) -> None:
    """Marks a task as completed."""
    task.status = "completed"


def calculate_task_cost(task: Task) -> float:
    """Calculates the estimated labor cost for a task."""
    total = task.hourly_rate * task.estimated_hours
    return round_currency(total)
