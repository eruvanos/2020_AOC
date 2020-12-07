import re
from collections import defaultdict
from typing import List, Dict, NamedTuple

BAG_PATTERN = re.compile(r"(\d) ([^,.]*) bag")


class Rule(NamedTuple):
    amount: int
    color: str


def part_1(data: Dict[str, Rule]):
    # revert rules
    lookups: Dict[str, List] = defaultdict(list)
    for color, rules in data.items():
        for rule in rules:
            lookups[rule.color].append(color)

    options = set()
    to_check = ["shiny gold"]
    while len(to_check) > 0:
        color = to_check.pop()
        parents = lookups[color]
        for parent in parents:
            if parent in options:
                continue
            else:
                options.add(parent)
                to_check.append(parent)
    return len(options)


def part_2(data: Dict[str, Rule]):
    def count_bags(color):
        result = 1
        for child in data[color]:
            child: Rule
            result += child.amount * count_bags(child.color)
        return result

    total = count_bags("shiny gold")
    return total - 1


def parse(lines):
    rules: Dict[str, List] = {}

    for line in lines:
        rule_color, rest = line.split(" bags contain ")

        rules[rule_color] = []
        for amount, color in BAG_PATTERN.findall(rest):
            rules[rule_color].append(Rule(int(amount), color))

    return rules


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    data = parse(lines)
    print("Part 1: ", part_1(data))
    print("Part 2: ", part_2(data))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
