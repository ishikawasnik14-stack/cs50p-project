import pytest

from project import add, subtract, multiply, divide, calculate


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 5) == 3


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 2) == 4.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_calculate():
    assert calculate(5, "+", 3) == 8
    assert calculate(5, "-", 3) == 2
    assert calculate(5, "*", 3) == 15
    assert calculate(6, "/", 3) == 2


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate(5, "%", 3)