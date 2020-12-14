from pathlib import Path

import pytest
from pytest import param

import solution
from solution import permut

files = [
    ("test_input.txt", 165, None),
    ("test_input2.txt", None, 208),
]


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, expected, _ in files],
)
def test_part_1(file: Path, expected):
    if expected is None:
        return
    lines = file.read_text().splitlines()

    result = solution.part_1(solution.parse(lines))
    assert result == expected


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, _, expected in files],
)
def test_part_2(file: Path, expected):
    if expected is None:
        return
    lines = file.read_text().splitlines()

    result = solution.part_2(solution.parse(lines))
    assert result == expected


def test_permut():
    assert list(permut("XX")) == ["00", "01", "10", "11"]
    assert list(permut("X1X")) == ["010", "011", "110", "111"]
    assert list(permut("1X0XX")) == [
        "10000",
        "10001",
        "10010",
        "10011",
        "11000",
        "11001",
        "11010",
        "11011",
    ]
