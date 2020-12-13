from pathlib import Path

import pytest
from pytest import param

import solution
from utils.vector import Vector

files = [
    ("test_input.txt", 25, 286),
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


def test_rotation():
    vec = Vector(1, 2)

    assert Vector(2, -1) == vec.rotate_degree(90)
    assert Vector(-1, -2) == vec.rotate_degree(180)
    assert Vector(-2, 1) == vec.rotate_degree(-90)
