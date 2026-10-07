"""
Unit tests for order management and totals.
"""

import pytest
from app.orders import create_order, add_item_to_order, get_order_subtotal, get_order_total


def test_create_order():
    """Verify new order initialization."""
    order = create_order("ORD-101", "Alice Smith")
    assert order.order_id == "ORD-101"
    assert order.customer_name == "Alice Smith"
    assert len(order.items) == 0
    assert order.status == "created"


def test_add_item_to_order():
    """Verify adding line items to order."""
    order = create_order("ORD-102", "Bob Jones")
    item = add_item_to_order(order, "Monitor", 150.0, 1)
    assert len(order.items) == 1
    assert item.item_name == "Monitor"
    assert item.unit_price == 150.0


def test_order_total_with_multi_quantity_items():
    """Verify complete order calculation with multiple units, discount, and tax."""
    order = create_order("ORD-103", "Charlie Brown")
    add_item_to_order(order, "USB Cable", 10.0, 5)   # 10 * 5 = 50.0
    add_item_to_order(order, "HDMI Cable", 20.0, 2)  # 20 * 2 = 40.0
    # Expected subtotal = 90.0
    # 10% discount = 9.0 -> Taxable = 81.0
    # 10% tax = 8.10 -> Total expected = 89.10
    total = get_order_total(order, discount_percent=10.0, tax_rate=10.0)
    assert total == 89.10, f"Expected total 89.10, got {total}"


def test_empty_order_total():
    """Verify empty order total is zero."""
    order = create_order("ORD-104", "Empty Order")
    total = get_order_total(order)
    assert total == 0.0
