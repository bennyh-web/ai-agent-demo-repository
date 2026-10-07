"""
Utility functions for validation and currency formatting.
"""


def validate_positive_amount(amount: float, name: str = "amount") -> float:
    """Validates that a financial amount is strictly positive."""
    if amount <= 0:
        raise ValueError(f"{name} must be greater than zero, got {amount}")
    return float(amount)


def validate_positive_quantity(quantity: int, name: str = "quantity") -> int:
    """Validates that a quantity is a positive integer."""
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError(f"{name} must be a positive integer, got {quantity}")
    return quantity


def round_currency(value: float) -> float:
    """Rounds currency to 2 decimal places."""
    return round(float(value), 2)


def format_currency(value: float) -> str:
    """Formats a float as standard USD currency string."""
    return f"${value:.2f}"
