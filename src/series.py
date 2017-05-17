"""This module has three functions that return the nth term of a series."""


def fibonacci(n):
    """Function that provides nth term of a fibonacci series."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Function that provides the nth term of lucas series."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    """Function that uses a required parameter and two optional parameters."""
    if n == 1:
        return x
    elif n == 2:
        return y
    return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)

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
