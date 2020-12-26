# https://www.youtube.com/watch?v=Q5TvCyu4RUo&ab_channel=KarstenMorisse
# fmt: off
import sys
from collections import defaultdict

sys.path.append("..")

# fmt: on
from colorama import init

init()

DEBUG = False

_print = print


def print(*args, **kw):
    if DEBUG:
        _print(*args, **kw)


def combinations(first, second):
    """
    creates set of string from concatenation of each character in first
    to each character in second
    """
    return {(f, s) for f in first for s in second}


def cyk(rules, msg):
    reverse_lookup = defaultdict(list)
    for r, rs in rules.items():
        for rss in rs:
            reverse_lookup[tuple(rss)].append(r)

    table = defaultdict(set)
    n = len(msg)

    # fill table
    # N[i,j]
    # i: column, j: row
    for x in range(n):
        for y in range(n - x):
            table[(x, y)] = set()  # use set for deduplication

    print()
    for l in msg:
        print(l.rjust(10), end="")
    print()

    # fill lookups from msg
    for x in range(n):
        value = reverse_lookup[tuple(msg[x])]
        table[(x, 0)] = value
        print(",".join(table[(x, y)]).rjust(10), end="")
    print()

    # fill lines:
    for y in range(1, n):
        for x in range(n - y):

            # collect combinations
            for k in range(y):
                for cs in combinations(table[x, k], table[x + k + 1, y - k - 1]):
                    found_rule = reverse_lookup[cs]
                    for v in found_rule:
                        table[(x, y)].add(v)

            print(",".join(table[(x, y)]).rjust(10), end="")
        print()

    return "0" in table[x, y]


def part_1(data):
    rules, msg_lines = data

    valid = 0
    for msg in msg_lines:
        result = cyk(rules, msg)
        if result:
            valid += 1

    return valid


def part_2(data):
    rules, msg_lines = data

    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]

    valid = 0
    for msg in msg_lines:
        # result = validate(rules, msg)
        result = cyk(rules, msg)
        # print(f"{Fore.GREEN if result else Fore.RED}{msg}")
        if result:
            valid += 1

    return valid
    # return sum(1 for msg in msg_lines if validate(rules, msg))


def parse(lines):
    rule_lines = []
    while lines and (line := lines.pop(0)):
        rule_lines.append(line)

    msg_lines = []
    while lines and (line := lines.pop(0)):
        msg_lines.append(line)

    def parse_rule(rule):
        parts = rule.split(" | ")
        if "a" in parts[0] or "b" in parts[0]:
            return parts[0][1]
        else:
            return [part.split(" ") for part in parts]

    rules = {
        r: parse_rule(parts) for r, parts in map(lambda l: l.split(": "), rule_lines)
    }

    return rules, msg_lines


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
