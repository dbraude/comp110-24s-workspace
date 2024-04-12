"""Example recursive function."""
__author__ = "730704898"


def f(n: int, k: int) -> int:
    """Multiplication by recursion."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)