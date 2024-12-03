import pytest

from aoc2024 import day2, utils


@pytest.mark.parametrize(
    "report,safe",
    zip(
        utils.read_fixture("test/day2-star1.txt"),
        [True, False, False, False, False, True],
        strict=True,
    ),
)
def test_analyze_report(report: str, safe: bool):
    assert day2.report_safety(utils.extract_ints(report)) == safe


@pytest.mark.parametrize(
    "report,safe",
    zip(
        utils.read_fixture("test/day2-star1.txt"),
        [True, False, False, True, True, True],
        strict=True,
    ),
)
def test_analyze_report_dampener(report: str, safe: bool):
    assert day2.report_safety_dampener(utils.extract_ints(report)) == safe


def test_first_star():
    assert day2.first_star("real/day2-star1.txt") == 383


def test_second_star():
    assert day2.second_star("real/day2-star1.txt") == 436
