import pytest

from aoc2024 import day5

RULES_TEST_CASES = (
    ((75, 47, 61, 53, 29), True),
    ((97, 61, 53, 29, 13), True),
    ((75, 29, 13), True),
    ((75, 97, 47, 61, 53), False),
    ((61, 13, 29), False),
    ((97, 13, 75, 29, 47), False),
)

SORT_TEST_CASES = (
    ((75, 97, 47, 61, 53), (97, 75, 47, 61, 53)),
    ((61, 13, 29), (61, 29, 13)),
    ((97, 13, 75, 29, 47), (97, 75, 47, 29, 13)),
)


@pytest.fixture
def rules():
    rules, _ = day5.parse_input("test/day5-star1.txt")
    return rules


@pytest.mark.parametrize(("test_case", "expected"), RULES_TEST_CASES)
def test_valid_rules(rules, test_case, expected):
    assert day5.valid_page_set(rules, test_case) == expected


def test_middle(rules):
    assert sum([day5.middle_if_valid(rules, tc) for tc, _ in RULES_TEST_CASES]) == 143


@pytest.mark.parametrize(("unsorted", "_sorted"), SORT_TEST_CASES)
def test_sort(rules, unsorted, _sorted):
    assert day5.sort_page_ordering(rules, unsorted) == _sorted


def test_sum_what_needs_sorting(rules):
    assert day5.sum_what_needs_sorting(rules, [x[0] for x in SORT_TEST_CASES]) == 123


def test_first_star():
    assert day5.first_star() == 5948


def test_second_star():
    assert day5.second_star() == 3062
