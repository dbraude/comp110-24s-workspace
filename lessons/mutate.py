"""Mutating functions."""
__author__ = "730704898"


def manual_append(a: list[int], b: int) -> None:
    """Appends int to the end of an int list."""
    a.append(b)


def double(a: list[int]) -> None:
    """Doubles the value of every item in an int list."""
    i = 0
    while i < len(a):
        a[i] *= 2
        i += 1
