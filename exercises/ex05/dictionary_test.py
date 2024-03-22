"""Tests for dictionaries."""
__author__ = "730704898"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_use() -> None:
    """Tests usage of invert function with an dict that will raise no errors."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use_empty() -> None:
    """Tests usage of an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_edge_key_error() -> None:
    """Tests if the invert function raises an index error when there are duplicate keys in the inverted dictionary."""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {'a': 'y', 'b': 'y', 'c': 'x'}
        invert(test_dict)


def test_favorite_color_use() -> None:
    """Tests usage of favorite color function that will raise no errors."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_use_tie() -> None:
    """Tests that in the event of a tie in popularity the first color to reach the highest frequency is selected."""
    assert favorite_color({"Me": "yellow", "Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "yellow"


def test_favorite_color_edge_empty() -> None: 
    """Tests the edge case that the dictionary of people and colors is empty."""
    assert favorite_color({}) == ""


def test_count_use() -> None:
    """Tests usage of count function that will raise no errors."""
    assert count(["Bob", "Jane", "Tofu", "Tofu", "The return of Jafar"]) == {"Bob": 1, "Jane": 1, "Tofu": 2, "The return of Jafar": 1}


def test_count_use_frequency() -> None:
    """Tests usage of count in which terms appear more than once with an equal frequency."""
    assert count(["Bob", "Jane", "Jane", "Tofu", "Tofu", "The return of Jafar"]) == {"Bob": 1, "Jane": 2, "Tofu": 2, "The return of Jafar": 1}


def test_count_edge_empty() -> None:
    """Tests the edge case that the list of items is empty."""
    assert count([]) == {}


def test_alphabetizer_use() -> None:
    """Tests usage of alphabetizer function that will raise no errors."""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_use_mixed_case() -> None: 
    """Tests that the alphabetizer function still works when words contain mixed case."""
    assert alphabetizer(["Python", "sugar", "Turtle", "party", "table"]) == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_alphabetizer_edge_empty() -> None:
    """Tests the edge case that the list of items is empty."""
    assert alphabetizer([]) == {}


def test_update_attendance_use() -> None:
    """Tests usage of attendance function with no errors."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    assert attendance_log == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_use_new_day() -> None: 
    """Tests adding a new day to the attendance log."""
    attendance_log: dict[str, list[str]] = {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}
    update_attendance(attendance_log, "Sunday", "Me")
    assert attendance_log == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Sunday': ['Me']}


def test_update_attendance_edge_duplicates() -> None:
    """Tests if the attendance log does not change when adding a duplicate name to a day."""
    attendance_log: dict[str, list[str]] = {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}
    update_attendance(attendance_log, "Tuesday", "Alyssa")
    assert attendance_log == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}