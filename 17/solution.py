# fmt: off
import sys
from collections import Counter
from functools import lru_cache
from typing import Set

sys.path.append("..")


# fmt: on


@lru_cache
def calc_neighbors_3d(vec):
    vx, vy, vz, vw = vec

    ns = set()
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                nx, ny, nz = vx + x, vy + y, vz + z
                if (nx, ny, nz) != (vx, vy, vz):
                    ns.add((nx, ny, nz, vw))
    return set(ns)


@lru_cache
def calc_neighbors_4d(vec_4d):
    vx, vy, vz, vw = vec_4d

    ns = set()
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                for w in (-1, 0, 1):
                    nx, ny, nz, nw = vx + x, vy + y, vz + z, vw + w
                    if (nx, ny, nz, nw) != (vx, vy, vz, vw):
                        ns.add((nx, ny, nz, nw))
    return set(ns)


def debug(state: Set):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0
    min_w = 0
    max_w = 0
    for x, y, z, w in state:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_z = min(min_z, z)
        max_z = max(max_z, z)
        min_w = min(min_w, w)
        max_w = max(max_w, w)

    print()
    for w in range(min_w, max_w + 1):
        for z in range(min_z, max_z + 1):
            print(f"{z=} {w=}")
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    print("#" if (x, y, z, w) in state else ".", end="")
                print()
        print("========================")


def step(cells: Set, neigbor_factory):
    new_state = set()
    all_neighbors = Counter()

    # calc active cells
    for cell in cells:
        ns = neigbor_factory(cell)

        for n in ns:
            all_neighbors[n] += 1

        active_ns = len(cells.intersection(ns))
        if active_ns in (2, 3):
            new_state.add(cell)

    # spawn new cells
    for n, value in all_neighbors.items():
        if value == 3:
            new_state.add(n)

    return new_state


def part_1(cells):
    state: Set = cells
    # debug(state)

    for _ in range(6):
        state = step(state, calc_neighbors_3d)
        # debug(state)

    return len(state)


def part_2(cells):
    state: Set = cells
    # debug(state)

    for _ in range(6):
        state = step(state, calc_neighbors_4d)
        # debug(state)

    return len(state)


def parse(lines):
    cubes = set()
    z = 0
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == "#":
                cubes.add((x, y, z, 0))

    return cubes


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
