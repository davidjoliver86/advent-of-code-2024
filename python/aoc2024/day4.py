"""
Day 4: Ceres Search
"""

from collections.abc import Iterable

from . import utils


def find_matches(text: Iterable[str], pattern: str) -> list[int, int]:
    """
    Find matches word-search style across a given rectangular array of text. Searches
    horizontally, vertically, and diagonally, both forwards and backwards.

    Args:
        text (Iterable[str]): Lines of the rectangle of text.
        pattern (str): The pattern to search for.

    Returns:
        list[int, int]: List of column,row coordinates of matches.
    """
    # Define values
    height = len(text)
    width = len(text[0])
    pattern_len = len(pattern)
    found = []
    matches = set((tuple(ch for ch in pattern), tuple(ch for ch in pattern)[::-1]))

    # Horizontal
    for row_index in range(height):
        for col_index in range(width - pattern_len + 1):
            candidate = tuple(
                text[row_index][col_index + offset] for offset in range(pattern_len)
            )
            if candidate in matches:
                found.append((col_index, row_index))

    # Vertical
    for col_index in range(width):
        for row_index in range(height - pattern_len + 1):
            candidate = tuple(
                text[row_index + offset][col_index] for offset in range(pattern_len)
            )
            if candidate in matches:
                found.append((col_index, row_index))

    # Diagonal Forward
    for row_index in range(height - pattern_len + 1):
        for col_index in range(width - pattern_len + 1):
            candidate = tuple(
                text[row_index + offset][col_index + offset]
                for offset in range(pattern_len)
            )
            if candidate in matches:
                found.append((col_index, row_index))
    # Diagonal Backward
    for row_index in range(height - pattern_len + 1):
        for col_index in range(pattern_len - 1, width):
            candidate = tuple(
                text[row_index + offset][col_index - offset]
                for offset in range(pattern_len)
            )
            if candidate in matches:
                found.append((col_index, row_index))
    return found


def find_cross_mas(text: Iterable[str]) -> list[int, int]:
    """
    Finds diagonal cross-pairings of "MAS" across a given rectangular array of text.
    Each "MAS" can be forwards or backwards, independently. For example:

    M.S
    .A.
    M.S

    Args:
        text (Iterable[str]): Lines of the rectangle of text.

    Returns:
        list[int, int]: List of column,row coordinates of matches.
    """
    height = len(text)
    width = len(text[0])
    found = []
    for row_index in range(height - 2):
        for col_index in range(width - 2):
            upper_left = text[row_index][col_index]
            upper_right = text[row_index][col_index + 2]
            center = text[row_index + 1][col_index + 1]
            lower_left = text[row_index + 2][col_index]
            lower_right = text[row_index + 2][col_index + 2]
            if center == "A" and (
                (
                    upper_left == "M"
                    and upper_right == "S"
                    and lower_left == "M"
                    and lower_right == "S"
                )
                or (
                    upper_left == "S"
                    and upper_right == "M"
                    and lower_left == "S"
                    and lower_right == "M"
                )
                or (
                    upper_left == "M"
                    and upper_right == "M"
                    and lower_left == "S"
                    and lower_right == "S"
                )
                or (
                    upper_left == "S"
                    and upper_right == "S"
                    and lower_left == "M"
                    and lower_right == "M"
                )
            ):
                found.append((col_index + 1, row_index + 1))
    return found


def first_star(text: Iterable[str]):
    return len(find_matches(text, "XMAS"))


def second_star(text: Iterable[str]):
    return len(find_cross_mas(text))


def main():  # pragma: no cover
    data = [line.strip() for line in utils.read_fixture("real/day4-star1.txt")]
    print(first_star(data))
    print(second_star(data))


if __name__ == "__main__":
    main()  # pragma: no cover
