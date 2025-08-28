from __future__ import annotations

from mpmath import mp as _mp


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def sqrt(a: float) -> float:
    """Return the square root of `a`.

    Uses mpmath for consistent precision. Raises a ValueError for negative input.

    Args:
        a: Non-negative number to compute the square root for.

    Returns:
        float: The square root of `a`.

    Raises:
        ValueError: If `a` is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    # _mp.sqrt returns an mpf; convert to float for compatibility with other functions
    return float(_mp.sqrt(a))
