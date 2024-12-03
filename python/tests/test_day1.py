from aoc2024 import day1, utils


def test_compute_distances():
    first, second = day1.make_transposed_lists(
        utils.read_fixture("test/day1-star1.txt")
    )
    assert day1.compute_distances(first, second) == 11


def test_similarity_score():
    first, second = day1.make_transposed_lists(
        utils.read_fixture("test/day1-star1.txt")
    )
    assert day1.similarity_score(first, second) == 31


def test_first_star():
    assert day1.first_star("real/day1-star1.txt") == 1873376


def test_second_star():
    assert day1.second_star("real/day1-star1.txt") == 18997088
