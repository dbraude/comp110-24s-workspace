"""Test my garden functions."""
__author__ = "730704898"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_use() -> None:
    """Tests use case of adding a new plant to an already existing plant kind."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "flower", "daisy")
    assert by_kind == {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}


def test_add_by_kind_duplicate() -> None:
    """Tests edge case of adding in a plant to a category that already contains it."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "flower", "marigold")
    assert by_kind == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}


def test_add_by_date_use() -> None:
    """Tests use case of adding in a plant to a new date and an attached plant."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(by_date, "May", "elderberry")
    assert by_date == {'April': ['marigold'], 'June': ['carrots'], 'May': ['elderberry']}


def test_add_by_date_duplicate() -> None:
    """Tests edge case of adding in a plant to a date that already contains it."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(by_date, "April", "marigold")
    assert by_date == {'April': ['marigold'], 'June': ['carrots']}


def test_lookup_by_kind_and_date_use() -> None:
    """Tests whether the lookup by kind and date function prints a list containing the kind at the correct date."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    assert lookup_by_kind_and_date(by_kind, by_date, "flower", "April") == "flowers to plant in April: ['marigold']"


def test_lookup_by_kind_and_date_no_kind() -> None:
    """Tests whether the function returns an error the when the date being looked up doesn't exist."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    assert lookup_by_kind_and_date(by_kind, by_date, "flower", "November") == AssertionError