"""
Day 1: Historian Hysteria
"""

from collections import Counter
from collections.abc import Iterable

from . import utils


def extract_ints(string: str) -> tuple[int]:
    """
    Extracts integers out of a string that may contain multiple integers separated by
    whitespace.

    Args:
        string (str): The string to extract ints from.

    Returns:
        tuple[int]: The ints that were extracted.
    """
    return tuple(int(x) for x in string.split())


def make_transposed_lists(lines: Iterable[str]) -> tuple[tuple[int], tuple[int]]:
    """
    From the data provided, transpose the data such that there is one list for each
    column with all the values converted to ints. Assumes there will be two columns.

    Args:
        lines (Iterable[str]): Iterable containing the text to create the transposed
        lists from.

    Returns:
        tuple[tuple[int], tuple[int]]: The transposed lists of numbers as ints.
    """
    nums = [extract_ints(line) for line in lines]
    return tuple(zip(*nums, strict=True))


def compute_distances(first: Iterable[int], second: Iterable[int]) -> int:
    """
    For each pair of numbers in the lists, find the sum of the absolute values of the
    differences between each pair of numbers, starting with pairs of the smallest number
    in each list, then the next smallest, and so forth.

    Args:
        first (Iterable[int]): The first list.
        second (Iterable[int]): The second list.

    Returns:
        int: The sum of all absolute values of differences from each sorted list.
    """
    return sum(abs(a - b) for a, b in zip(sorted(first), sorted(second), strict=True))


def similarity_score(first: Iterable[int], second: Iterable[int]) -> int:
    """
    Calculate a total similarity score by adding up each number in the first list after
    multiplying it by the number of times that number appears in the second list.

    Args:
        first (Iterable[int]): The first list.
        second (Iterable[int]): The second list.

    Returns:
        int: The total similarity score.
    """
    counts = Counter(second)
    return sum(val * counts.get(val, 0) for val in first)


def first_star(fixture: str):
    return compute_distances(*make_transposed_lists(utils.read_fixture(fixture)))


def second_star(fixture: str):
    return similarity_score(*make_transposed_lists(utils.read_fixture(fixture)))


if __name__ == "__main__":
    print(first_star("real/day1-star1.txt"))  # pragma: no cover
    print(second_star("real/day1-star1.txt"))  # pragma: no cover
