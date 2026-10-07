"""
Unit tests for pricing calculations.
"""

import pytest
from app.models import OrderItem
from app.pricing import (
    calculate_item_cost,
    calculate_order_subtotal,
    calculate_discount,
    calculate_tax,
)


def test_calculate_item_cost_multi_unit():
    """Verify that item cost multiplies unit price by quantity."""
    unit_price = 25.0
    quantity = 4
    expected_cost = 100.0  # 25.0 * 4 = 100.0
    actual_cost = calculate_item_cost(unit_price, quantity)
    assert actual_cost == expected_cost, (
        f"Expected item cost to be {expected_cost} (unit_price * quantity), but got {actual_cost}"
    )


def test_calculate_order_subtotal():
    """Verify order subtotal aggregates multiple line items correctly."""
    items = [
        OrderItem("Keyboard", 20.0, 3),  # 20 * 3 = 60.0
        OrderItem("Mousepad", 15.0, 2),  # 15 * 2 = 30.0
    ]
    expected_subtotal = 90.0  # 60 + 30 = 90.0
    actual_subtotal = calculate_order_subtotal(items)
    assert actual_subtotal == expected_subtotal, (
        f"Expected subtotal {expected_subtotal}, got {actual_subtotal}"
    )


def test_calculate_discount():
    """Verify discount calculation percentage."""
    subtotal = 200.0
    discount = calculate_discount(subtotal, 10.0)
    assert discount == 20.0


def test_calculate_tax():
    """Verify sales tax percentage."""
    amount = 100.0
    tax = calculate_tax(amount, 8.0)
    assert tax == 8.0
