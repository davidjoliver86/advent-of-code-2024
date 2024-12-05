"""
Day 5: Print Queue
"""

import operator
from collections import defaultdict
from collections.abc import Iterable

from . import utils

type Rules = defaultdict[set[int]]
type PageSet = Iterable[int]


def parse_input(path: str) -> tuple[Rules, list[PageSet]]:
    """
    Take the puzzle input and return the page ordering rules and the sets of pages to
    produce in each update.

    Rules are represented as a dictionary of sets, the key being the page ordering that
    comes before a given page, and the page numbers in the set being those that come
    after it.

    Args:
        path (str): Path to the fixture file.

    Returns:
        tuple[Rules, list[PageSet]]: The rules and page sets parsed from the input.
    """
    rules = defaultdict(set[int])
    page_sets = []
    passed_split = False
    for line in utils.read_fixture(path):
        if line == "\n":
            passed_split = True
            continue
        if not passed_split:
            before, after = (int(x) for x in line.split("|"))
            rules[before].add(after)
        else:
            page_sets.append(tuple(int(x) for x in line.split(",")))
    return rules, page_sets


def valid_page_set(rules: Rules, page_set: PageSet) -> bool:
    """
    Determines if a given page set is valid according to the rules. For each successive
    pairing of two page numbers in the page set, the ordering rules must remain valid
    throughout.

    Args:
        rules (Rules): The page ordering rules.
        page_set (PageSet): The pages to produce.

    Returns:
        bool: Whether the pages in the page set conform to the ordering rules.
    """
    for index in range(len(page_set) - 1):
        before, after = page_set[index], page_set[index + 1]
        if after not in rules[before]:
            return False
    return True


def middle_if_valid(rules: Rules, page_set: PageSet) -> int:
    """
    If the page set is determined to be valid, take the median page number in the page
    set. Assumes that the length of the page set is odd. If not valid, returns 0.

    Args:
        rules (Rules): The page ordering rules.
        page_set (PageSet): The pages to produce.

    Returns:
        int: The median page number in the page_set if it's valid, else 0.
    """
    if valid_page_set(rules, page_set):
        return page_set[(len(page_set) - 1) // 2]
    return 0


def sort_page_ordering(rules: Rules, page_set: PageSet) -> PageSet:
    """
    Takes a page set that may not necessarily be in the correct order and returns the
    pages in the order they should be in. For each page number, see how many rules are
    in the set of rules when compared to all other page numbers in the set. The pages
    with the most number of matches must logically come earliest in the order, and so
    forth.

    Args:
        rules (Rules): The page ordering rules.
        page_set (PageSet): The pages to produce.

    Returns:
        PageSet: The ordered pages.
    """
    score = {}
    for index, page in enumerate(page_set):
        before_and_after = page_set[:index] + page_set[index + 1 :]
        score[page] = sum([1 if bna in rules[page] else 0 for bna in before_and_after])

    return tuple(
        x[0] for x in sorted(score.items(), key=operator.itemgetter(1), reverse=True)
    )


def sum_what_needs_sorting(rules: Rules, page_sets: Iterable[PageSet]) -> int:
    """
    For a collection of page sets that may not necessarily be in the correct order,
    return the summed median of the *post-sorted* page sets, but *only* among those page
    sets that needed to be sorted.

    Args:
        rules (Rules): The page ordering rules.
        page_set (PageSet): The pages to produce.

    Returns:
        int: The summed medians of the page sets, after sorting, that needed to be
        sorted.
    """
    total = 0
    for page_set in page_sets:
        if not valid_page_set(rules, page_set):
            total += middle_if_valid(rules, sort_page_ordering(rules, page_set))
    return total


def first_star():
    rules, page_sets = parse_input("real/day5-star1.txt")
    return sum(middle_if_valid(rules, page_set) for page_set in page_sets)


def second_star():
    rules, page_sets = parse_input("real/day5-star1.txt")
    return sum_what_needs_sorting(rules, page_sets)


def main():  # pragma: no cover
    print(first_star())
    print(second_star())


if __name__ == "__main__":
    main()  # pragma: no cover
