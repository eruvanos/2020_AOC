from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 295, 1068781),
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
    lines = file.read_text().splitlines()

    result = solution.part_2(solution.parse(lines))
    assert result == expected


def test_part_2_plus():
    assert solution.chines([3, 1, 6], [5, 7, 8]) == 78
    assert solution.chines([2, 3, 2], [3, 4, 5]) == 47

    assert solution.part_2((None, "17,x,13,19".split(","))) == 3417
    assert solution.part_2((None, "67,7,59,61".split(","))) == 754018
    assert solution.part_2((None, "67,x,7,59,61".split(","))) == 779210
    assert solution.part_2((None, "67,7,x,59,61".split(","))) == 1261476
    assert solution.part_2((None, "1789,37,47,1889".split(","))) == 1202161486
