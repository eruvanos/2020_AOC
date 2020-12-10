from functools import lru_cache
from typing import List

from pydantic.utils import defaultdict


def part_1(data: List[int]):
    data = list(sorted(data))
    device_jolt = max(data) + 3

    occ = defaultdict(int)
    for low, high in zip([0] + data, data + [device_jolt]):
        diff = high - low
        occ[diff] += 1

    return occ[1] * occ[3]


def part_2(data):
    data = list(sorted(data))
    device_jolt = max(data) + 3

    jolts = [0] + data + [device_jolt]
    lookup = set(jolts)

    @lru_cache
    def count_options(i):
        if i == device_jolt:
            return 1

        options = 0
        for n in range(i + 1, i + 4):
            if n in lookup:
                options += count_options(n)
        # print(i, '->', options)
        return options

    return count_options(0)


def parse(lines):
    return [int(l) for l in lines]


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
