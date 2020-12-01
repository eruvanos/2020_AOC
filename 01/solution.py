def part_1(numbers):
    for n in numbers:
        for m in numbers:
            if n + m == 2020:
                print(n, m)
                return n * m


def part_2(numbers):
    min_value = min(numbers)

    for n in numbers:
        for m in numbers:
            if n + m + min_value < 2020:
                for k in numbers:
                    if n + m + k == 2020:
                        print(n, m, k)
                        return n * m * k


def main(puzzle_input_f):
    numbers = [int(l.strip()) for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(numbers))
    print("Part 2: ", part_2(numbers))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
