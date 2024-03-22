"""Summing the elements of a list using different loops."""
__author__ = "730704898"


def w_sum(vals: list[float]) -> float:
    """Returns sum of a float list with a while loop."""
    i: int = 0
    final: float = 0
    while (i < len(vals)):
        final += vals[i]
        i += 1
    return final


def f_sum(vals: list[float]) -> float:
    """Returns the sum of a float list with for loop."""
    final: float = 0
    for v in vals:
        final += v
    return final


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of a float list with a for range loop."""
    final: float = 0
    for i in range(0, len(vals)):
        final += vals[i]
    return final