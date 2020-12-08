from collections import deque
from pathlib import Path
from typing import List, Tuple


class Machine:
    def __init__(self, code: List[Tuple]):
        self.code = code

        self.pc = 0
        self.acc = 0

        self.term = False
        self.debug = False
        self.history: deque = deque()

    @staticmethod
    def from_lines(lines):
        code = Machine.parse_lines(lines)
        return Machine(code)

    @staticmethod
    def parse_lines(lines):
        code = [tuple(x.split()) for x in lines]
        return code

    @staticmethod
    def from_file(file):
        lines = Path(file).read_text().splitlines()
        return Machine.from_lines(lines)

    @staticmethod
    def from_machine(machine: "Machine"):
        m = Machine(machine.code[:])
        m.pc = machine.pc
        m.acc = machine.acc
        m.term = machine.term
        m.debug = machine.debug
        m.history = deque(machine.history)
        return m

    def step(self, debug=False):
        if self.term:
            return

        self.history.append((self.pc, self.acc))

        op, arg = self.code[self.pc]
        fun = getattr(self, f"do_{op}", self.err)
        fun(int(arg))

        if self.debug or debug:
            print(f"{self.pc}, {self.acc} - {op} {arg}")

        if self.pc >= len(self.code):
            self.term = True

    def undo(self):
        self.pc, self.acc = self.history.pop()

    def do_acc(self, arg):
        self.pc += 1
        self.acc += arg

    def do_jmp(self, arg):
        self.pc += arg

    def do_nop(self, arg):
        self.pc += 1

    def err(self, line):
        raise Exception(f"Can not execute: {self.code[self.pc]}")
