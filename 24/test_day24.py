from pathlib import Path

import pytest
from pytest import param

import solution
from tiles import Grid
from utils.vector import Vector

files = [
    ("test_input.txt", 10, 2208),
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


def test_example():
    assert Grid().walk_and_flip("esew").tiles == {Vector(1, -1)}
    assert Grid().walk_and_flip("nwwswee").tiles == {Vector(0, 0)}
