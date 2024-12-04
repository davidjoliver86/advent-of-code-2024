import pytest

from aoc2024 import day3, utils

TEST_CASE_1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST_CASE_2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


@pytest.fixture
def real_program():
    _fixture = utils.read_fixture("real/day3-star1.txt")
    return day3.parse_program("".join(line for line in _fixture))


@pytest.mark.parametrize(
    ("test_case", "dos_and_donts", "expected"),
    ((TEST_CASE_1, False, 161), (TEST_CASE_2, True, 48)),
)
def test_run_program_without_dos_donts(
    test_case: str, dos_and_donts: bool, expected: int
):
    """
    Tests that the parsed program returns the values provided with or without taking
    into consideration the do() and don't() calls.

    Args:
        test_case (str): The test case to check.
        dos_and_donts (bool): Whether to consider the do() and don't() calls.
        expected (int): The expected output of the program.
    """
    assert day3.run_program(day3.parse_program(test_case), dos_and_donts) == expected


def test_first_star(real_program):
    assert day3.first_star(real_program) == 161289189


def test_second_star(real_program):
    assert day3.second_star(real_program) == 83595109
