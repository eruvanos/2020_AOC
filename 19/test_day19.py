from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 2, None),
    ("test_input2.txt", 3, 12),
]


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, expected, _ in files],
)
def test_part_1(file: Path, expected):
    print()
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


def test_check_line():
    rules_1 = {0: "12", 1: "a", 2: "b"}
    assert solution.check(rules_1, "ab")
    assert not solution.check(rules_1, "ba")


def test_parse():
    assert solution.parse(["0: 1 2", "1: a", "2: b", "3: 1 2 | 2 1"])[0] == {
        "0": [["1", "2"]],
        "1": "a",
        "2": "b",
        "3": [["1", "2"], ["2", "1"]],
    }


def test_paper_example():
    rules, _ = solution.parse(["0: 1 2", "1: 3 4", "2: 4 3", '3: "a"', '4: "b"'])

    assert solution.cyk(rules, "abba")
    assert not solution.cyk(rules, "bbba")


def test_complex_paper_example():
    rules, _ = solution.parse(
        ["0: 1 2", "1: 3 4 | 4 3", "2: 3 4 | 4 3", '3: "a"', '4: "b"']
    )

    assert solution.cyk(rules, "abba")
    assert not solution.cyk(rules, "bbba")


def test_part2_in_detail():
    print()
    lines = Path("test_input2.txt").read_text().splitlines()
    rules, messages = solution.parse(lines)

    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["500", "31"]]
    rules["500"] = [["42", "11"]]

    assert solution.cyk(rules, "babbbbaabbbbbabbbbbbaabaaabaaa")


def test_youtube_example():
    print()
    rules, _ = solution.parse(
        ["0: 1 2 | 2 3", "1: 2 1 | a", "2: 3 3 | b", "3: 1 2 | a"]
    )

    assert solution.cyk(rules, "abaab")
