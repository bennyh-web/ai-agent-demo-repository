"""
Domain models for Task and Order Management System.
"""

from typing import List, Dict, Any, Optional


class Task:
    """Represents a work task assigned to a team member."""

    def __init__(
        self,
        task_id: str,
        title: str,
        hourly_rate: float,
        estimated_hours: int,
        status: str = "pending"
    ):
        self.task_id = task_id
        self.title = title
        self.hourly_rate = hourly_rate
        self.estimated_hours = estimated_hours
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "hourly_rate": self.hourly_rate,
            "estimated_hours": self.estimated_hours,
            "status": self.status,
        }


class OrderItem:
    """Represents a line item in a customer order."""

    def __init__(self, item_name: str, unit_price: float, quantity: int):
        self.item_name = item_name
        self.unit_price = unit_price
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item_name": self.item_name,
            "unit_price": self.unit_price,
            "quantity": self.quantity,
        }


class Order:
    """Represents a customer order containing multiple order items."""

    def __init__(
        self,
        order_id: str,
        customer_name: str,
        items: Optional[List[OrderItem]] = None,
        status: str = "created"
    ):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items: List[OrderItem] = items if items is not None else []
        self.status = status

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "items": [it.to_dict() for it in self.items],
            "status": self.status,
        }
