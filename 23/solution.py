# fmt: off
import sys

from tqdm import tqdm

from cups import Cups

sys.path.append("..")


# fmt: on


def part_1(data, rounds=100):
    cups = Cups(data)

    for r in range(rounds):

        repr_cups = cups.to_str()

        # pick cups
        cups.pick()

        # select destination
        destination = cups.dest()

        # log round
        print(f"-- move {r + 1} --")
        print(repr_cups)
        print("pick up:", *[p for p in cups.picked])
        print("destination:", destination)
        print()

        # place cups
        cups.place(destination)

        # next cur
        cups.next()

    return "".join(map(str, cups.cups(1)[1:]))


def part_2(numbers):
    CUPS = 1_000_000
    ROUNDS = 10_000_000

    next_number = max(numbers) + 1
    for n in range(CUPS - len(numbers)):
        numbers.append(next_number)
        next_number += 1

    cups = Cups(numbers)

    for r in tqdm(range(ROUNDS)):
        cups.pick()
        destination = cups.dest()
        cups.place(destination)
        cups.next()

    node_1 = cups.lookup[1]
    return node_1.ref.number * node_1.ref.ref.number


def parse(lines):
    numbers = [int(l) for l in lines.pop(0)]
    return numbers


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
