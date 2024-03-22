"""Dictionary utility functions."""
__author__ = "730704898"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values for a dictionary."""
    output: dict[str, str] = {}
    for key in input:
        if input[key] in output:
            raise KeyError("KeyError")
        output[input[key]] = key
        
    return output


def favorite_color(input: dict[str, str]) -> str:
    """Cycles through a dictionary of names and colors and prints the most popular color."""
    color_tally: dict[str, int] = {}
    for key in input:
        if input[key] not in color_tally:
            color_tally[input[key]] = 1
        else:
            color_tally[input[key]] += 1
    top_count: int = 0
    current_count: int = 0
    most_popular: str = ""

    for key in color_tally:
        current_count = color_tally[key]
        if current_count > top_count:
            top_count = current_count
            most_popular = key
    
    return most_popular


def count(input: list[str]) -> dict[str, int]:
    """Counts the amount each word in a list of strings appears and returns a dictionary with the tallies."""
    tally: dict[str, int] = {}

    for key in input: 
        if key in tally:
            tally[key] += 1
        else:
            tally[key] = 1
    
    return tally


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Takes in a list of strings and returns a dictionary of the strings by their first letter."""
    output: dict[str, list[str]] = {}

    for word in input:
        if word[0].lower() not in output: 
            output[word[0].lower()] = []
        output[word[0].lower()].append(word)

    return output


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates an exitsting list of attendance by adding new students to each day of the dictionary."""
    if day not in input:
        input[day] = []
    if student not in input[day]:
        input[day].append(student)