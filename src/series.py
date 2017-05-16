"""This module returns an nth term of a series."""


def fibonacci(n):
    """Function that provides nth term of a fibonacci series."""
    x, y = 0, 1
    for i in range(n - 1):
        x, y = y, x + y
    return x


def lucas(n):
    """Function that provides the nth term of lucas series."""
    x, y = 2, 1
    for i in range(n - 1):
        x, y = y, x + y
    return x
