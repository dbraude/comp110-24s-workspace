"""Splitting a dictionary into two lists."""
__author__ = "730704898"


def get_keys(input: dict[str, int]) -> list[str]:
    """Gets the keys of a dictionary and returns them as a list of strings."""
    output: list[str] = []
    for key in input:
        output.append(key)
    return output


def get_values(input: dict[str, int]) -> list[int]:
    """Get the values of a dictionary and returns them as a list of ints."""
    output: list[int] = []
    for key in input:
        output.append(input[key])
    return output