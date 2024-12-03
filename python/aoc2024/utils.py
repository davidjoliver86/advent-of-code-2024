"""
General purpose utilities and helpers.
"""

import pathlib
from collections.abc import Generator


def read_fixture(path: str) -> Generator[str, str, str]:
    """
    Reads a fixture from the 'fixtures' folder given a relative path underneath it.

    Args:
        path (str): Path relative to the fixtures folder.

    Returns:
        TextIO: The open file.

    Yields:
        Iterator[TextIO]: Lines from the open file.
    """
    fixture = pathlib.Path(__file__).parents[2] / "fixtures" / path
    with fixture.open("r", encoding="utf-8") as fp:
        yield from fp
