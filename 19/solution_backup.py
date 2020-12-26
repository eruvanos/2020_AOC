# fmt: off
import sys
from dataclasses import dataclass, field
from typing import List, Tuple

from call_stack import gs

sys.path.append("..")

# fmt: on

from colorama import init, Fore

init()


class Node:
    def check(self, line) -> Tuple[bool, str]:
        pass


@dataclass
class Rule(Node):
    name: str
    seqs: List[List[Node]] = field(default_factory=list)

    def add(self, rule_set: List["Node"]):
        self.seqs.append(rule_set)

    def check(self, line):
        for i, sub_rules in enumerate(self.seqs):
            with gs.frame(f"{self.name}[{i}]"):
                match, rest = Rule.check_subrules(sub_rules, line)
                gs.log(match, rest)
                if match:
                    return True, rest
        return False, line

    @staticmethod
    def check_subrules(sub_rules, line):
        rest = line
        for sub_rule in sub_rules:
            match, rest = sub_rule.check(rest)
            if not match:
                break
        else:
            return True, rest

        return False, line

    def simple_repr(self, node: Node):
        if isinstance(node, Letter):
            return node.l
        if isinstance(node, Rule):
            return str(node.name)
        if isinstance(node, List):
            return f"[{','.join(map(self.simple_repr, node))}]"
        else:
            return repr(node)

    def __repr__(self):
        return f"<{self.name}>[{'|'.join(map(self.simple_repr, self.seqs))}]"


@dataclass
class Letter(Node):
    l: str

    def check(self, line):
        with gs.frame(self.l):
            if len(line) == 0:
                gs.log("EOL")
                return False, line
            if line[0] == self.l:
                gs.log("Matched", line)
                return True, line[1:]
            else:
                gs.log("Skip")
                return False, line

    def __repr__(self):
        return self.l


def part_1(data):
    with gs.frame("part_1"):
        rule_objects, msg_lines = data
        start_rule = rule_objects["0"]

        counter = 0

        for msg in msg_lines:
            match, rest = start_rule.check(msg)
            gs.log((Fore.GREEN if match else Fore.RED) + msg, match)
            if match and len(rest) == 0:
                counter += 1
        return counter


def part_2(data):
    print()
    with gs.frame("part_2"):
        rule_objects, msg_lines = data

        r8 = rule_objects["8"]
        r42 = rule_objects["42"]
        r11 = rule_objects["11"]
        r31 = rule_objects["31"]

        r8.seqs = [[r42], [r42, r8]]
        r11.seqs = [[r42, r31], [r42, r11, r31]]

        return part_1(data)


def parse(lines):
    rule_lines = []
    while lines and (line := lines.pop(0)):
        rule_lines.append(line)

    msg_lines = []
    while lines and (line := lines.pop(0)):
        msg_lines.append(line)

    # parse rule_lines
    rules = {}
    rule_objects = {}

    # a,b rules
    for line in rule_lines[:]:
        number, rest = line.split(": ")
        if "a" in rest or "b" in rest:
            letter = rest[1]
            rules[number] = letter
            rule_objects[number] = Letter(letter)
            rule_lines.remove(line)

    # rules containing ref to other rules
    while rule_lines and (line := rule_lines.pop(0)):
        number, rest = line.split(": ")

        # sub_rules
        rules[number] = []
        sub_rules = rest.split(" | ")

        new_rule = rule_objects.setdefault(number, Rule(number))
        for sub_rule in sub_rules:
            refs = sub_rule.split(" ")
            rules[number].append(refs)

            new_rule.add([rule_objects.setdefault(ref, Rule(ref)) for ref in refs])

    for r, s in sorted(rules.items(), key=lambda x: int(x[0])):
        print(r, str(s))

    return rule_objects, msg_lines


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
