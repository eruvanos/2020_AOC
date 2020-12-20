from pathlib import Path

import pytest
from pytest import param

import solution
from interpreter import Lexer, Interpreter
from solution import Value, Add, Mul

files = [
    ("test_input.txt", 26335, 51 + 46 + 1445 + 669060 + 23340),
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


def test_nodes():
    assert Add(Value(3), Value(5)).eval() == 8
    assert Mul(Value(3), Value(5)).eval() == 15
    assert Mul(Add(Value(3), Value(5)), Value(5)).eval() == 40


def test_eval_par():
    assert solution.eval_par("1+2+3") == ["1", "+", "2", "+", "3"]
    assert solution.eval_par("1+(2+3)") == ["1", "+", ["2", "+", "3"]]
    assert False


def test_eval_add():
    assert solution.eval_par(["1", "+", "2", "+", "3"]) == [
        ["1", "+", [["2", "+", "3"]]]
    ]
    assert False


def test_interpreter():
    assert Interpreter(Lexer("1 + (2 * 3) + (4 * (5 + 6))")).expr() == 51
    assert Interpreter(Lexer("2 * 3 + (4 * 5)")).expr() == 46
