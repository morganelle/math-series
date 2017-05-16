'''Fibonacci testing.'''
import pytest


PARAMS_TABLE = [
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


@pytest.mark.parametrize('n, result', PARAMS_TABLE)
def test_fibonacci(n, result):
    '''Tests fibonacci functions'''
    from series import fibonacci
    assert fibonacci(n) == result
