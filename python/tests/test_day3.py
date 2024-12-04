import pytest

from aoc2024 import day3, utils

TEST_CASE = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


@pytest.fixture
def real_program():
    _fixture = utils.read_fixture("real/day3-star1.txt")
    return day3.parse_program("".join(line for line in _fixture))


def test_parse_functions():
    assert day3.run_program(day3.parse_program(TEST_CASE), False) == 161


def test_first_star(real_program):
    assert day3.first_star(real_program) == 161289189


def test_second_star(real_program):
    assert day3.second_star(real_program) == 83595109
