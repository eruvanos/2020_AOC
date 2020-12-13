import sys

sys.path.append("..")

from utils.vector import Vector
from utils.directions import NESW_VEC, TURN_LEFT, TURN_RIGHT


def part_1(cmds):
    ship = Vector(0, 0)
    face = "E"
    for dir, steps in cmds:

        if dir == "F":
            dir = face

        if dir in NESW_VEC:
            ship += NESW_VEC[dir] * steps
        elif dir == "R":
            for _ in range(steps // 90):
                face = TURN_RIGHT[face]
        elif dir == "L":
            for _ in range(steps // 90):
                face = TURN_LEFT[face]
        else:
            raise Exception(f"Unknown instruction {(dir, steps)}")

    return abs(ship.x) + abs(ship.y)


def part_2(cmds):
    ship = Vector(0, 0)
    waypoint = Vector(10, 1)
    for dir, steps in cmds:

        if dir == "F":
            ship += waypoint * steps

        elif dir in NESW_VEC:
            waypoint += NESW_VEC[dir] * steps
        elif dir == "R":
            waypoint = waypoint.rotate_degree(steps)
        elif dir == "L":
            waypoint = waypoint.rotate_degree(-steps)
        else:
            raise Exception(f"Unknown instruction {(dir, steps)}")

    return abs(ship.x) + abs(ship.y)


def parse(lines):
    lines = [(l[:1], int(l[1:])) for l in lines]
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
