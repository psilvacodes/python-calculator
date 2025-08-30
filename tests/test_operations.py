"""Unit tests for calculator.operations."""

import pytest

from calculator.operations import add, divide, multiply, sqrt, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    import pytest

    with pytest.raises(ValueError):
        divide(1, 0)


# def test_add_fail():
#     assert add(2, 2) == 5  # intentionally wrong


def test_sqrt_positive():
    assert sqrt(9) == pytest.approx(3.0)


def test_sqrt_zero():
    assert sqrt(0) == pytest.approx(0.0)


def test_sqrt_negative_raises():
    with pytest.raises(ValueError):
        sqrt(-1)
