"""
Task Manager Application
A project task management and cost calculation utility.
"""

from typing import List, Dict, Any, Optional


def calculate_task_cost(price: float, quantity: int) -> float:
    """
    Calculate the total cost for a task based on unit price and quantity.

    INTENTIONAL BUG:
    Incorrectly uses addition (price + quantity) instead of multiplication (price * quantity).
    """
    return price + quantity


class Task:
    def __init__(self, task_id: int, title: str, price_per_hour: float, hours: int, status: str = "pending"):
        self.task_id = task_id
        self.title = title
        self.price_per_hour = price_per_hour
        self.hours = hours
        self.status = status

    def get_cost(self) -> float:
        """Calculate the total cost for this specific task."""
        return calculate_task_cost(self.price_per_hour, self.hours)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "price_per_hour": self.price_per_hour,
            "hours": self.hours,
            "cost": self.get_cost(),
            "status": self.status,
        }


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task_id: int, title: str, price_per_hour: float, hours: int) -> Task:
        task = Task(task_id, title, price_per_hour, hours)
        self.tasks.append(task)
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def calculate_total_project_cost(self) -> float:
        """Calculates total cost across all tasks in the project."""
        return sum(task.get_cost() for task in self.tasks)


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task(1, "Database Migration", price_per_hour=50.0, hours=4)
    print(f"Total Project Cost: ${manager.calculate_total_project_cost():.2f}")
