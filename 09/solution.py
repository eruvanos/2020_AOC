def check(slice, number):
    for i, n in enumerate(slice):
        for m in slice[i + 1 :]:
            if n + m == number:
                return True
    return False


def part_1(data):
    pre_amble = 25 if len(data) > 20 else 5

    for i, n in enumerate(data[pre_amble:]):
        start = 0 + i
        end = start + pre_amble

        if not check(data[start:end], n):
            break
    return n


def part_2(data):
    invalid_number = part_1(data)

    for i, n in enumerate(data):
        count = n
        for j, m in enumerate(data[i + 1 :]):
            count += m
            if count > invalid_number:
                break
            elif count == invalid_number:
                slice = data[i : 2 + i + j]
                return min(slice) + max(slice)

    return None


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
