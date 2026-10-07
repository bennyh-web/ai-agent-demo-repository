"""
Unit tests for Task Manager Application.
Tests verify task cost calculations and project totals.
"""

import pytest
import sys
import os

# Add current dir to sys.path so tests can import task_manager
sys.path.insert(0, os.path.dirname(__file__))

from task_manager import calculate_task_cost, Task, TaskManager


def test_calculate_task_cost_standalone():
    """Verify that standalone task cost multiplies price by quantity."""
    price = 25.0
    quantity = 4
    expected_cost = 100.0  # 25.0 * 4 = 100.0
    actual_cost = calculate_task_cost(price, quantity)
    assert actual_cost == expected_cost, (
        f"Expected cost to be {expected_cost} (price * quantity), but got {actual_cost}"
    )


def test_task_instance_cost():
    """Verify that a Task instance calculates cost correctly."""
    task = Task(task_id=1, title="UI Development", price_per_hour=40.0, hours=5)
    expected_cost = 200.0  # 40.0 * 5 = 200.0
    assert task.get_cost() == expected_cost, (
        f"Expected task cost to be {expected_cost}, but got {task.get_cost()}"
    )


def test_task_manager_total_project_cost():
    """Verify that TaskManager aggregates multiple tasks correctly."""
    manager = TaskManager()
    manager.add_task(task_id=101, title="API Setup", price_per_hour=50.0, hours=2)     # 50 * 2 = 100
    manager.add_task(task_id=102, title="Unit Testing", price_per_hour=30.0, hours=3)  # 30 * 3 = 90
    expected_total = 190.0  # 100 + 90 = 190.0
    actual_total = manager.calculate_total_project_cost()
    assert actual_total == expected_total, (
        f"Expected total project cost to be {expected_total}, but got {actual_total}"
    )
