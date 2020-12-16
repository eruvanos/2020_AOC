# fmt: off
import sys

sys.path.append("..")


# fmt: on


def has_any_valid_rule(rules, number):
    for name, min1, max1, min2, max2 in rules:
        if min1 <= number <= max1 or min2 <= number <= max2:
            return True

    return False


def valid_for_every_number(rule, numbers):
    name, min1, max1, min2, max2 = rule
    for number in numbers:
        if not (min1 <= number <= max1 or min2 <= number <= max2):
            return False

    return True


def part_1(data):
    rules, our_ticket, nearby_tickets = data

    error_rate = 0
    for ticket in nearby_tickets:
        for number in ticket:
            if not has_any_valid_rule(rules, number):
                error_rate += number

    return error_rate


def part_2(data):
    rules, our_ticket, nearby_tickets = data

    # remove invalid tickets
    for ticket in nearby_tickets[:]:
        for number in ticket:
            if not has_any_valid_rule(rules, number):
                nearby_tickets.remove(ticket)

    # determine rule columns
    our_ticket_resolved = {}
    left_rules = rules[:]
    while left_rules:
        for column, values in enumerate(zip(*nearby_tickets)):
            valid_rules = list(
                filter(lambda r: valid_for_every_number(r, values), left_rules)
            )
            if len(valid_rules) == 1:
                determined_rule = valid_rules[0]
                # print(f"{column}: {determined_rule}")
                left_rules.remove(determined_rule)
                our_ticket_resolved[determined_rule[0]] = our_ticket[column]

    assert len(left_rules) == 0

    # parse ticket
    total = 1
    for rule, value in our_ticket_resolved.items():
        if rule.startswith("departure"):
            total *= value

    return total


def parse(lines):
    # rules
    rules = []
    while line := lines.pop(0):
        name, rest = line.split(": ")
        r1, r2 = rest.split(" or ")
        min1, max1 = r1.split("-")
        min2, max2 = r2.split("-")
        rules.append((name, int(min1), int(max1), int(min2), int(max2)))

    # your ticket
    assert "your ticket:" == lines.pop(0)
    numbers = map(int, lines.pop(0).split(","))
    our_ticket = tuple(numbers)
    assert "" == lines.pop(0)

    # nearby tickets
    assert "nearby tickets:" == lines.pop(0)
    nearby_tickets = []
    while lines and (line := lines.pop(0)):
        numbers = map(int, line.split(","))
        nearby_tickets.append(tuple(numbers))

    return rules, our_ticket, nearby_tickets


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
