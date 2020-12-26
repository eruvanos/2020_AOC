# fmt: off
import sys

from tiles import Grid, simulate

sys.path.append("..")


# fmt: on


def part_1(data):
    grid = Grid()

    for seq in data:
        grid.walk_and_flip(seq)

    return len(grid.tiles)


def part_2(data):
    grid = Grid()
    for seq in data:
        grid.walk_and_flip(seq)

    # start game of life
    state = grid.tiles
    for r in range(100):
        state = simulate(state)
        # print(f"Day {r+1:2.0f}: {len(state)}")

    return len(state)


def parse(lines):
    # lines = [int(l) for l in lines]
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
