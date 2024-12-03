"""
Day 2: Red-Nosed Reports
"""

import collections
from collections.abc import Iterable

from . import utils


def report_safety(levels: Iterable[int]) -> bool:
    """
    A report is a string of integers representing "levels". A report only counts as safe
    if both of the following are true:

    * The levels are either all increasing or all decreasing.
    * Any two adjacent levels differ by at least one and at most three.

    Args:
        levels (Iterable[int]): The reports' levels.

    Returns:
        bool: Whether the report is considered safe.
    """
    differences = [levels[index + 1] - level for index, level in enumerate(levels[:-1])]
    increasing_safely = min(differences) >= 1 and max(differences) <= 3
    decreasing_safely = max(differences) <= -1 and min(differences) >= -3
    return increasing_safely or decreasing_safely


def report_safety_dampener(levels: Iterable[int]) -> bool:
    """
    Pass the report through the report safety check function. If the report is unsafe,
    try different combinations of removing one item from the report, and if any of them
    are safe, consider the report safe via the Problem Dampener.

    Args:
        levels (Iterable[int]): The reports' levels.

    Returns:
        bool: Whether the report - or at least one permutation of reports with one level
        removed - is considered safe.
    """
    if report_safety(levels):
        return True
    for index in range(len(levels)):
        copied_levels = list(levels)
        copied_levels.pop(index)
        if report_safety(copied_levels):
            return True
    return False


def first_star(fixture: str):
    results = (
        report_safety(utils.extract_ints(report))
        for report in utils.read_fixture(fixture)
    )
    return collections.Counter(results)[True]


def second_star(fixture: str):
    results = (
        report_safety_dampener(utils.extract_ints(report))
        for report in utils.read_fixture(fixture)
    )
    return collections.Counter(results)[True]


if __name__ == "__main__":
    print(first_star("real/day2-star1.txt"))  # pragma: no cover
    print(second_star("real/day2-star1.txt"))  # pragma: no cover
