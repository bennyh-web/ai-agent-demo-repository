"""
Unit tests for task service.
"""

import pytest
from app.task_service import create_task, complete_task, calculate_task_cost


def test_create_task():
    """Verify task creation with properties."""
    task = create_task("TSK-1", "Design Landing Page", 75.0, 4)
    assert task.task_id == "TSK-1"
    assert task.title == "Design Landing Page"
    assert task.hourly_rate == 75.0
    assert task.estimated_hours == 4
    assert task.status == "pending"


def test_complete_task():
    """Verify marking task complete."""
    task = create_task("TSK-2", "Setup CI Pipeline", 60.0, 2)
    complete_task(task)
    assert task.status == "completed"


def test_calculate_task_cost():
    """Verify task labor cost calculation."""
    task = create_task("TSK-3", "Security Audit", 100.0, 5)
    cost = calculate_task_cost(task)
    assert cost == 500.0
