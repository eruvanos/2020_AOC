from collections import Counter


def part_1(data):

    total = 0
    for group in data:
        total += len(list(Counter("".join(group)).keys()))

    return total


def part_2(data):
    total = 0
    for group in data:
        counts = Counter("".join(group))

        for answer, count in counts.items():
            if count == len(group):
                total += 1

    return total


def parse(lines):
    groups = []
    group = []
    groups.append(group)

    for line in lines:
        if len(line) == 0:
            group = []
            groups.append(group)
        else:
            group.append(line)

    return groups


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
