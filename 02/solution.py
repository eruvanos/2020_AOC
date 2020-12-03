from collections import Counter


def part_1(entries):
    valid = 0
    for mini, maxi, letter, pw in entries:
        if mini <= Counter(pw)[letter] <= maxi:
            valid += 1

    return valid


def part_2(entries):
    valid = 0
    for mini, maxi, letter, pw in entries:

        if Counter(pw[mini - 1] + pw[maxi - 1])[letter] == 1:
            valid += 1

    return valid


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]

    entries = []
    for l in lines:
        rule, letter, pw = l.split(" ")
        mini, maxi = rule.split("-")
        mini = int(mini)
        maxi = int(maxi)

        letter = letter.replace(":", "")
        entries.append((mini, maxi, letter, pw))

    print("Part 1: ", part_1(entries))
    print("Part 2: ", part_2(entries))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
