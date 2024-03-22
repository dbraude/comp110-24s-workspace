"""Some functions for my garded plan!"""
__author__ = "730704898"


def add_by_kind(input: dict[str, list[str]], kind: str, name: str) -> None:
    """Add a plant under an array of plants of its kind."""
    if kind not in input:
        input[kind] = []
    if name not in input[kind]:
        input[kind].append(name)


def add_by_date(input: dict[str, list[str]], date: str, name: str) -> None:
    """Add a plant under and array of plants of its month."""
    if date not in input:
        input[date] = []
    if name not in input[date]:
        input[date].append(name) 


def lookup_by_kind_and_date(kind_dict: dict[str, list[str]], date_dict: dict[str, list[str]], kind: str, date: str) -> str:
    """Crossreference plants and dates and find plants of a certain kind from a certain date."""
    assert kind in kind_dict
    assert date in date_dict
    output: list[str] = []

    plants_of_this_kind: list[str] = kind_dict[kind]
    for plant in plants_of_this_kind:
        if plant in date_dict[date]:
            output.append(plant)
    if len(output) > 0:
        return f"{kind}s to plant in {date}: {output}"
    return f"No {kind}s to plant in {date}."