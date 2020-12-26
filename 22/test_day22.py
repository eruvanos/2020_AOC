from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 306, 291),
]


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, expected, _ in files],
)
def test_part_1(file: Path, expected):
    lines = file.read_text().splitlines()

    result = solution.part_1(solution.parse(lines))
    assert result == expected


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, _, expected in files],
)
def test_part_2(file: Path, expected):
    print()
    lines = file.read_text().splitlines()

    result = solution.part_2(solution.parse(lines))
    assert result == expected


@pytest.mark.timeout(2)
def test_prevent_loop():
    print()
    solution.part_2(([43, 19], [2, 29, 14]))
