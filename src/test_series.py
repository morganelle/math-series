"""Fibonacci testing."""
import pytest


PARAMS_TABLE = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


@pytest.mark.parametrize('n', PARAMS_TABLE)
def test_fibonacci(n):
    from series import fibonacci
    assert fibonacci(n) == PARAMS_TABLE[n - 1]
