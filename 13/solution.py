# fmt: off
import sys

sys.path.append("..")

# fmt: on


from itertools import count
from math import ceil


def part_1(data):
    timestamp, plan = data
    busses = [int(l) for l in plan if l != "x"]

    min_wait = 100000000
    min_bus = None

    for bus in busses:
        dep = ceil(timestamp / bus) * bus
        wait = dep - timestamp

        if wait < min_wait:
            min_bus = bus
            min_wait = wait

    return min_bus * min_wait


def chines(bis, mods):
    N = 1
    for n in mods:
        N *= n
    print("N:", N)

    binixi_sum = 0

    print("bi", "Ni", "xi")
    for delay, m in zip(bis, mods):
        bi = m - delay

        # calc ni
        n = N // m

        # calc xi
        for x in count():
            if x * n % m == 1:
                break

        binixi = bi * n * x

        print(bi, n, x, binixi)
        binixi_sum += binixi

    result = binixi_sum % N
    print(f"chines: {result}")

    # check
    # for bi, m in zip(bis, mods):
    #     assert result % m == bi

    return result


def part_2(data):
    _, plan = data

    # parse rules
    print("Rules")
    bis = []
    mods = []
    for delay, bus in enumerate(plan):
        if bus == "x":
            continue
        else:
            print(delay, bus)
            bis.append(delay)
            mods.append(int(bus))

    return chines(bis, mods)


def parse(lines):
    timestamp = int(lines[0])
    busses = [l for l in lines[1].split(",")]
    return timestamp, busses


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
