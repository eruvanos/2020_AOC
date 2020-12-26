# fmt: off
import sys
from itertools import count

sys.path.append("..")


# fmt: on
def transform(subject, loop_size):

    value = 1
    for _ in range(loop_size):
        value *= subject
        value %= 20201227

    return value


def reverse(subject, cypher):
    value = 1
    for loop_size in count(1):
        value *= subject
        value %= 20201227

        if value == cypher:
            break
    return loop_size


def part_1(data):
    door_pub, card_pub = data

    door_loop_size = reverse(7, door_pub)
    card_loop_size = reverse(7, card_pub)

    encryption_key1 = transform(door_pub, card_loop_size)
    encryption_key2 = transform(card_pub, door_loop_size)

    assert encryption_key1 == encryption_key2
    return encryption_key1


def part_2(data):
    pass


def parse(lines):
    lines = [int(l) for l in lines]
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
