# fmt: off
import sys
from dataclasses import dataclass
from typing import Callable

from interpreter import Lexer, Interpreter

sys.path.append("..")


# fmt: on


class Node:
    def eval(self):
        return


@dataclass
class Value(Node):
    value: int

    def eval(self):
        return self.value

    def __repr__(self):
        return f"{self.value}"


class Op(Node):
    a: Node
    b: Node = None
    op: Callable

    def eval(self):
        return self.op(self.a.eval(), self.b.eval())


@dataclass
class Add(Op):
    a: Node
    b: Node = None
    op: Callable = int.__add__

    def eval(self):
        return self.op(self.a.eval(), self.b.eval())

    def __repr__(self):
        return f"({self.a}+{self.b})"


@dataclass
class Mul(Op):
    a: Node
    b: Node = None
    op: Callable[[Node, Node], int] = int.__mul__

    def eval(self):
        return self.op(self.a.eval(), self.b.eval())

    def __repr__(self):
        return f"({self.a}*{self.b})"


FACTORIES = {
    "+": Add,
    "*": Mul,
}


def process_v1(tokens, last_node):
    while tokens:
        token = tokens.pop(0)

        if last_node is None and token.isnumeric():
            last_node = Value(int(token))

        elif token.isnumeric():
            last_node.b = Value(int(token))

        elif token in FACTORIES:
            last_node = FACTORIES[token](last_node)

        elif last_node is None and token == "(":
            last_node = process_v1(tokens, None)

        elif token == "(":
            last_node.b = process_v1(tokens, None)

        elif token == ")":
            break

    return last_node


def part_1(data):
    total = 0
    for line in data:
        tokens = list(t for t in line if t != " ")
        result_node = process_v1(tokens, None)
        result = result_node.eval()
        total += result
        print(line, "=", result)

    return total


def part_2(data):
    total = 0
    for line in data:
        result = Interpreter(Lexer(line)).expr()
        total += result

    return total


def parse(lines):
    # lines = [int(l) for l in lines]
    return lines


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(parse(lines[:])))
    print("Part 2: ", part_2(parse(lines[:])))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
