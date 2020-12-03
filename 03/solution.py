from functools import reduce


class Map:
    def __init__(self, lines):
        self.lines = lines

    def get(self, x, y):
        if y >= len(self.lines):
            return None
        line = self.lines[y]
        return line[x % len(line)]


def part_1(data: Map, cx=3, cy=1):
    x = y = 0
    trees = 0
    while cell := data.get(x, y):
        trees += 1 if cell == "#" else 0

        x += cx
        y += cy

    return trees


def part_2(data: Map):
    results = [
        part_1(data, 1, 1),
        part_1(data, 3, 1),
        part_1(data, 5, 1),
        part_1(data, 7, 1),
        part_1(data, 1, 2),
    ]

    return reduce(int.__mul__, results, 1)


def parse(lines):
    return Map(lines)


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    data = parse(lines)
    print("Part 1: ", part_1(data))
    print("Part 2: ", part_2(data))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
