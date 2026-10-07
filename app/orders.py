"""
Order management service.
Handles order lifecycle and total cost calculations.
"""

from typing import Optional
from app.models import Order, OrderItem
from app.pricing import calculate_order_subtotal, calculate_order_total


def create_order(order_id: str, customer_name: str) -> Order:
    """Creates a new empty order."""
    if not order_id.strip():
        raise ValueError("Order ID cannot be empty")
    if not customer_name.strip():
        raise ValueError("Customer name cannot be empty")
    return Order(order_id=order_id, customer_name=customer_name)


def add_item_to_order(
    order: Order,
    item_name: str,
    unit_price: float,
    quantity: int
) -> OrderItem:
    """Adds a new line item to an existing order."""
    item = OrderItem(item_name=item_name, unit_price=unit_price, quantity=quantity)
    order.add_item(item)
    return item


def get_order_subtotal(order: Order) -> float:
    """Retrieves order subtotal from line items."""
    return calculate_order_subtotal(order.items)


def get_order_total(
    order: Order,
    discount_percent: float = 0.0,
    tax_rate: float = 0.0
) -> float:
    """Retrieves final order total including taxes and discounts."""
    return calculate_order_total(
        order.items,
        discount_percent=discount_percent,
        tax_rate=tax_rate
    )
