from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 37, 26),
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


def test_calc_neighbor_map_simple():
    seats = solution.parse(
        [
            ".............",
            ".L.L.#.#.#.#.",
            ".............",
        ]
    )
    nmap = solution.calc_neighbor_map(seats)

    assert nmap[(1, 1)] == {(3, 1)}


def test_calc_neighbor_map_2():
    seats = solution.parse(
        [
            ".......#.",
            "...#.....",
            ".#.......",
            ".........",
            "..#L....#",
            "....#....",
            ".........",
            "#........",
            "...#.....",
        ]
    )
    nmap = solution.calc_neighbor_map(seats)

    assert nmap[(3, 4)] == {
        (7, 0),
        (3, 1),
        (1, 2),
        (2, 4),
        (8, 4),
        (4, 5),
        (0, 7),
        (3, 8),
    }
