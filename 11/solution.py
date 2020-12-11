from collections import defaultdict
from typing import Dict

from pymunk import Vec2d

EMPTY = 0
FULL = 1

MAX_X = 0
MAX_Y = 0


def perm(*options):
    for a in options:
        for b in options:
            yield a, b


def round(seats: Dict[Vec2d, int], n_map, max_n=4):
    stable = True
    new_seats = {}
    for pos, seat in seats.items():

        neighbor = sum(seats.get(n, 0) for n in n_map[pos])
        if seat == EMPTY and neighbor == 0:
            new_seats[pos] = FULL
            stable = False
        elif seat == FULL and neighbor >= max_n:
            new_seats[pos] = EMPTY
            stable = False
        else:
            new_seats[pos] = seat

    return new_seats, stable


def debug(seats):
    print("================")
    for y in range(MAX_Y):
        for x in range(MAX_X):
            print(seats.get((x, y), "."), end="")
        print()


def part_1(seats):
    neighbor_map = {
        (x, y): {
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x + 1, y + 1),
        }
        for x, y in seats.keys()
    }

    stable = False
    while not stable:
        seats, stable = round(seats, neighbor_map)
        # debug(seats)
        # print("Stable:", stable)

    return sum(seats.values())


def calc_neighbor_map(seats):
    neighbor_map = defaultdict(set)
    for x, y in seats.keys():
        # horizontal
        if (neigh := calc_neighbor(seats, (x, y), -1, 0)) is not None:
            neighbor_map[(x, y)].add(neigh)
        if (neigh := calc_neighbor(seats, (x, y), 1, 0)) is not None:
            neighbor_map[(x, y)].add(neigh)

        # vertical
        if (neigh := calc_neighbor(seats, (x, y), 0, -1)) is not None:
            neighbor_map[(x, y)].add(neigh)
        if (neigh := calc_neighbor(seats, (x, y), 0, 1)) is not None:
            neighbor_map[(x, y)].add(neigh)

        # diagonals right
        if (neigh := calc_neighbor(seats, (x, y), 1, -1)) is not None:
            neighbor_map[(x, y)].add(neigh)
        if (neigh := calc_neighbor(seats, (x, y), 1, 1)) is not None:
            neighbor_map[(x, y)].add(neigh)

        # diagonals left
        if (neigh := calc_neighbor(seats, (x, y), -1, -1)) is not None:
            neighbor_map[(x, y)].add(neigh)
        if (neigh := calc_neighbor(seats, (x, y), -1, 1)) is not None:
            neighbor_map[(x, y)].add(neigh)

    return neighbor_map


def calc_neighbor(seats, pos, step_x, step_y):
    x, y = pos
    cx = x + step_x
    cy = y + step_y
    while 0 <= cx <= MAX_X and 0 <= cy <= MAX_Y:
        if (cx, cy) in seats:
            return (cx, cy)
        cx += step_x
        cy += step_y
    return None


def part_2(seats):
    stable = False
    while not stable:
        seats, stable = round(seats, calc_neighbor_map(seats), max_n=5)
        # debug(seats)
        # print("Stable:", stable)

    return sum(seats.values())


def parse(lines):
    seats = {}
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell in "L#":
                seats[(x, y)] = int(cell == "#")

    global MAX_X, MAX_Y
    MAX_X = x + 1
    MAX_Y = y + 1

    return seats


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
