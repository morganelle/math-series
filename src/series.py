"""This module has three functions that return the nth term of a series."""


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


def sum_series(n, x=0, y=1):
    """Function that uses a required parameter and two optional parameters."""
    for i in range(n - 1):
        x, y = y, x + y
    return x

if __name__ == "__main__":
    print()
    print("This module has 3 functions that return the nth term of a series:")
    print("Fibonacci, Lucas, or any series beginning with 2 optional values.")
    print("...\n")
    print("fibonacci(n):")
    print("    Returns the nth value in the Fibonacci series\n")
    print(">>> fibonacci(10):")
    print(fibonacci(10))
    print()
    print("lucas(n):")
    print("    Returns the nth value in the Lucas series\n")
    print(">>> lucas(10):")
    print(lucas(10))
    print()
    print("sum_series(n, x=0, y=1):")
    print("    Returns the nth value a series beginning with any two numbers.")
    print("    Without added params, it defaults to the Fibonacci sequence.\n")
    print(">>> sum_series(5):")
    print(sum_series(5))
    print(">>> sum_series(5, 2, 1):")
    print(sum_series(5, 2, 1))
    print(">>> sum_series(5, 3, 4):")
    print(sum_series(5, 3, 4))
