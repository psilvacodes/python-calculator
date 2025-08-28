import pytest

from calculator.operations import add, divide, multiply, subtract


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
