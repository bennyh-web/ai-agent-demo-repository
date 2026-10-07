"""
Pricing calculation service for items, orders, taxes, and discounts.
"""

from typing import List
from app.models import OrderItem
from app.utils import (
    validate_positive_amount,
    validate_positive_quantity,
    round_currency,
)


def calculate_item_cost(unit_price: float, quantity: int) -> float:
    """
    Calculate the total line cost for an item based on its unit price and quantity.

    Expected formula: unit_price * quantity
    """
    validate_positive_amount(unit_price, "unit_price")
    validate_positive_quantity(quantity, "quantity")

    # INTENTIONAL BUG: Uses addition instead of multiplication
    return unit_price + quantity


def calculate_order_subtotal(items: List[OrderItem]) -> float:
    """Calculates the subtotal for a list of order items."""
    total = sum(calculate_item_cost(item.unit_price, item.quantity) for item in items)
    return round_currency(total)


def calculate_discount(subtotal: float, discount_percent: float) -> float:
    """Calculates the discount amount based on percentage."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    discount = subtotal * (discount_percent / 100.0)
    return round_currency(discount)


def calculate_tax(amount: float, tax_rate: float) -> float:
    """Calculates sales tax based on percentage rate."""
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    tax = amount * (tax_rate / 100.0)
    return round_currency(tax)


def calculate_order_total(
    items: List[OrderItem],
    discount_percent: float = 0.0,
    tax_rate: float = 0.0
) -> float:
    """
    Calculates final order total applying subtotal, discount, and tax.
    """
    subtotal = calculate_order_subtotal(items)
    discount = calculate_discount(subtotal, discount_percent)
    taxable_amount = max(0.0, subtotal - discount)
    tax = calculate_tax(taxable_amount, tax_rate)
    return round_currency(taxable_amount + tax)
