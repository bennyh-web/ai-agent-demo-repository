# Task and Order Management System

A modular Python service for managing project tasks, order items, pricing calculations, and tax/discount aggregation.

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── models.py       # Domain entities: Task, OrderItem, Order
│   ├── pricing.py      # Pricing, discounts, tax, and item cost calculations
│   ├── orders.py       # Order lifecycle and totals calculation
│   ├── task_service.py # Task management and labor rate computation
│   └── utils.py        # Currency rounding and validation helpers
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_orders.py
│   ├── test_pricing.py
│   └── test_task_service.py
└── requirements.txt
```

## Running Tests

```bash
pytest
```
