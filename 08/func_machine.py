from pathlib import Path
from typing import NamedTuple, List, Tuple


class State(NamedTuple):
    code: List
    pc: int = 0
    acc: int = 0

    @property
    def term(self):
        return self.pc >= len(self.code)


def parse_line(line):
    op, arg = line.split()
    return op, int(arg)


def parse_lines(lines) -> List[Tuple]:
    code = [parse_line(l) for l in lines]
    return code


def from_lines(lines) -> State:
    code = parse_lines(lines)
    return State(code)


def from_file(file) -> State:
    lines = Path(file).read_text().splitlines()
    return from_lines(lines)


def step(state: State, debug=False):
    op_func = {
        "acc": do_acc,
        "jmp": do_jmp,
        "nop": do_nop,
    }

    if state.term:
        return state

    op, arg = state.code[state.pc]
    fun = op_func.get(op, err)
    new_state = fun(state, arg)

    if debug:
        print(f"{op} {arg} - {new_state.pc}, {new_state.acc}")

    return new_state


def run(self, debug=False):
    while not self.term:
        self.step(debug=debug)
    return self.acc


def do_acc(state, arg):
    return state._replace(pc=state.pc + 1, acc=state.acc + arg)


def do_jmp(state, arg):
    return state._replace(pc=state.pc + arg)


def do_nop(state, arg):
    return state._replace(pc=state.pc + 1)


def err(self, arg):
    raise Exception(f"Can not execute: {self.code[self.pc]}")
