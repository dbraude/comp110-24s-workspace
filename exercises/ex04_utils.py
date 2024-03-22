"""EX04 - List utlis functions."""
__name__ = "730704898"


def all(nums: list[int], target: int) -> bool:
    """Function that takes in an int list and returns true if the each number in the list is the target number."""
    if len(nums) == 0: 
        return False
    for i in nums:
        if i != target:
            return False
    return True


def max(input: list[int]) -> int:
    """Function that takes in an int list and returns the highest value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    highest: int = input[0]
    for i in input:
        if i > highest:
            highest = i
    return highest


def is_equal(list_1: list[int], list_2: list[int]) -> bool: 
    """Function that takes in 2 lists and determines whether they are equal."""
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Function that appends a list onto another list."""
    for i in range(len(list_2)):
        list_1.append(list_2[i])
