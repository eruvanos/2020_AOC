from collections import defaultdict


def part_1(data):
    max_id = 0
    for id, row, seat in data:
        max_id = max(id, max_id)

    return max_id


def part_2(data):
    rows = defaultdict(list)

    for id, row, seat in data:
        rows[row].append(seat)

    for row, seats in list(sorted(rows.items()))[2:]:
        if len(seats) < 8:
            for x in range(8):
                if x not in seats:
                    return row * 8 + x


def to_number(line):
    bin = "".join(["0" if l in "FL" else "1" for l in line])
    return int(f"0b{bin}", 2)


def _to_seat(line):
    row = to_number(line[:7])
    seat = to_number(line[7:])
    return row * 8 + seat, row, seat


def parse(lines):
    seats = []
    for line in lines:
        seats.append(_to_seat(line))

    return seats


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    data = parse(lines)

    assert _to_seat("BFFFBBFRRR") == (567, 70, 7)

    print("Part 1: ", part_1(data))
    print("Part 2: ", part_2(data))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
