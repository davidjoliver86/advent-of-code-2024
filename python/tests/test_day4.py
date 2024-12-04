from collections.abc import Iterable

import pytest

from aoc2024 import day4, utils

TEST_CASE = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()[1:]


def test_find_all():
    assert len(day4.find_matches(TEST_CASE, "XMAS")) == 18


def test_find_cross_mas():
    assert len(day4.find_cross_mas(TEST_CASE)) == 9


@pytest.fixture
def real_fixture():
    yield [line.strip() for line in utils.read_fixture("real/day4-star1.txt")]


def test_first_star(real_fixture: Iterable[str]):
    assert day4.first_star(real_fixture) == 2358


def test_second_star(real_fixture: Iterable[str]):
    assert day4.second_star(real_fixture) == 1737
