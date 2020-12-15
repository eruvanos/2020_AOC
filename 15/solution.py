# fmt: off
import sys
from time import sleep
from timeit import timeit

import tqdm

from utils.timer import Timer

sys.path.append("..")


# fmt: on


def part_1(data, stop=2020):
    bar = tqdm.tqdm(total=stop)

    # memory
    last_calls = {}
    last_number = None

    # init vars
    round = 0
    last_call = None

    # process input
    for round, n in enumerate(data, 1):
        bar.update()

        last_call = last_calls.get(n)
        last_calls[n] = round
        last_number = n

    # overcome
    for round in range(round + 1, stop + 1):
        bar.update()
        if last_call is None:
            m = 0
        else:
            m = round - 1 - last_call

        last_call = last_calls.get(m)
        last_calls[m] = round
        last_number = m

    bar.close()
    return last_number


def part_2(data):
    return part_1(data, stop=30000000)


def parse(lines):
    lines = [int(l) for l in lines[0].split(",")]
    return lines


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(parse(lines)))
    print("Part 2: ", part_2(parse(lines)))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
