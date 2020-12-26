from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 14897079, None),
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


@pytest.mark.timeout(2)
def test_reverse():
    door_pub = 17807724
    door_loop_size = solution.reverse(7, door_pub)
    assert door_loop_size == 11

    card_pub = 5764801
    card_loop_size = solution.reverse(7, card_pub)
    assert card_loop_size == 8
