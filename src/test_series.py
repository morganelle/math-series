"""Fibonacci testing."""
import pytest


FIB_TABLE = [
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34)
]


LUCAS_TABLE = [
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (6, 11),
    (7, 18),
    (8, 29),
    (9, 47),
    (10, 76)
]


SUM_TABLE = [
    (5, 2, 1, 7),
    (7, 2, 1, 18),
    (10, 2, 1, 76)
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    """Test fibonacci functions."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    """Test Lucas function."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_sum_series_fib(n, result):
    """Test sum series."""
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize('n, x, y, result', SUM_TABLE)
def test_sum_series_opt(n, x, y, result):
    """Test for optional sum series."""
    from series import sum_series
    assert sum_series(n, x, y) == result
