"""
Day 3: Mull It Over
"""

import re
from collections.abc import Iterable

from . import utils

DO = "do()"
DONT = "don't()"

R_DO = r"do\(\)"
R_DONT = r"don't\(\)"
R_MUL_FUNCTION = r"mul\((\d{1,3}),(\d{1,3})\)"

RE_MUL = re.compile(R_MUL_FUNCTION)
RE_EVERYTHING = re.compile(rf"{R_DO}|{R_DONT}|{R_MUL_FUNCTION}")


def parse_program(program: str) -> Iterable[re.Match]:
    """
    Parses the program for all do(), don't(), and mul(<int>,<int>) instructions.

    Args:
        program (str): The text of the program.

    Returns:
        Iterable[re.Match]: An iterable containing all matched tokens.
    """
    return RE_EVERYTHING.finditer(program)


def run_program(findings: Iterable[re.Match], dos_and_donts: bool) -> int:
    """
    Processes the program according to the tokens found. Sums up the value of all mul()
    function calls. If dos_and_donts is enabled, do() calls will enable the mul()
    function, and don't() calls will disable it. The mul() function starts enabled.

    Args:
        findings (Iterable[re.Match]): Iterable of re.Match objects from the parsed
        program.

        dos_and_donts (bool): Whether to process the do() and don't() calls (True), or
        ignore them (False).

    Returns:
        int: The sum of all parsed mul() functions according to the rules.
    """
    enabled = True
    total_sum = 0
    for finding in findings:
        _str = finding.group()
        if _str == DO:
            enabled = True
        elif _str == DONT:
            enabled = not dos_and_donts
        elif enabled:
            first, second = (int(x) for x in RE_MUL.search(_str).groups())
            total_sum += first * second
    return total_sum


def first_star(program: str):
    return run_program(program, False)


def second_star(program: str):
    return run_program(program, True)


def main():  # pragma: no cover
    _fixture = utils.read_fixture("real/day3-star1.txt")
    parsed = list(parse_program("".join(line for line in _fixture)))
    print(first_star(parsed))
    print(second_star(parsed))


if __name__ == "__main__":
    main()  # pragma: no cover
