import pytest
from Calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-7, 8, 1),
    (100, 200, 300),
    (3.5, 4.5, 8.0)
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (0, 7, -7),
    (-5, -10, 5),
    (7.5, 2.5, 5.0)
])
def test_subtract(a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 7, 21),
    (-2, 8, -16),
    (0, 123, 0),
    (1.5, 4, 6.0)
])
def test_multiply(a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (8, 4, 2),
    (20, 5, 4),
    (7, 2, 3.5),
    (10, 0, ValueError)
])
def test_divide(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calc.divide(a, b)
    else:
        assert calc.divide(a, b) == expected

@pytest.mark.parametrize("n, expected", [
    (5, True),
    (6, False),
    (11, True),
    (15, False),
    (19, True),
    (1, False)
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected
