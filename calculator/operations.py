"""Module calculator.operations.

Arithmetic operations for the python-calculator package.

Functions
---------
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
sqrt(a)
"""

from __future__ import annotations

from mpmath import mp as _mp


def add(a: float, b: float) -> float:
    """Return the sum of `a` and `b`.

    Args:
        a: First addend.
        b: Second addend.

    Returns:
        The sum of `a` and `b` as a float.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference `a - b`.

    Args:
        a: Minuend.
        b: Subtrahend.

    Returns:
        The result of `a - b` as a float.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product `a * b`.

    Args:
        a: First factor.
        b: Second factor.

    Returns:
        The product of `a` and `b` as a float.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient `a / b`.

    Args:
        a: Dividend.
        b: Divisor (must be non-zero).

    Returns:
        The quotient of `a` divided by `b` as a float.

    Raises:
        ZeroDivisionError: If `b` is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def sqrt(a: float) -> float:
    """Return the square root of `a`.

    Uses mpmath for consistent precision. Raises a ValueError for negative input.

    Args:
        a: Non-negative number to compute the square root for.

    Returns:
        The square root of `a` as a float.

    Raises:
        ValueError: If `a` is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    # _mp.sqrt returns an mpf; convert to float for compatibility with other functions
    return float(_mp.sqrt(a))
