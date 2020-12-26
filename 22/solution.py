# fmt: off
import sys
from itertools import count
from math import prod

sys.path.append("..")


# fmt: on


def part_1(data):
    p1_deck, p2_deck = data

    while p1_deck and p2_deck:
        p1 = p1_deck.pop(0)
        p2 = p2_deck.pop(0)
        print(p1, p2, "p1" if p1 > p2 else "p2")

        if p1 > p2:
            p1_deck.append(p1)
            p1_deck.append(p2)
        elif p2 > p1:
            p2_deck.append(p2)
            p2_deck.append(p1)
        else:
            raise Exception("Not Implemented")

    return sum(map(prod, zip(count(1), reversed(p1_deck + p2_deck))))


def game_hash(p1, p2):
    return ",".join(map(str, p1)) + "_" + ",".join(map(str, p2))


GAME_COUNTER = count(1)


def sub_game(p1_deck, p2_deck):
    game_number = next(GAME_COUNTER)
    print(f"New Game {game_number}: {p1_deck}, {p2_deck}")

    played_combos = set()
    round = count(1)
    while p1_deck and p2_deck:
        # prevent loops
        hash = game_hash(p1_deck, p2_deck)
        if hash in played_combos:
            print(
                f"G{game_number:2.0f}: {'P1' if bool(p1_deck) else 'P2'} [loop detected]"
            )
            print()
            return True, p1_deck, p2_deck
        else:
            played_combos.add(hash)

        game_round = next(round)

        p1 = p1_deck.pop(0)
        p2 = p2_deck.pop(0)
        print(
            f"G{game_number:2.0f} | {game_round :3.0f}:",
            p1,
            p2,
            "p1" if p1 > p2 else "p2",
        )

        if len(p1_deck) >= p1 and len(p2_deck) >= p2:
            print("-|")
            print()
            p1_won, *_ = sub_game(p1_deck[:p1], p2_deck[:p2])
            print(f"|- G{game_number:2.0f} | {game_round :3.0f}")

        else:
            assert p1 != p2
            p1_won = p1 > p2

        if p1_won:
            p1_deck.append(p1)
            p1_deck.append(p2)
        else:
            p2_deck.append(p2)
            p2_deck.append(p1)

    print(f"G{game_number:2.0f}: {'P1' if bool(p1_deck) else 'P2'}")
    print()
    return bool(p1_deck), p1_deck, p2_deck


def part_2(data):
    p1_deck, p2_deck = data

    p1_won, p1_deck, p2_deck = sub_game(p1_deck, p2_deck)

    print("Post_Game:")
    print("P1:", p1_deck)
    print("P2:", p2_deck)
    return sum(map(prod, zip(count(1), reversed(p1_deck + p2_deck))))


def parse(lines):
    assert lines.pop(0) == "Player 1:"
    p1_deck = []
    while line := lines.pop(0):
        p1_deck.append(int(line))

    assert lines.pop(0) == "Player 2:"
    p2_deck = []
    while lines and (line := lines.pop(0)):
        p2_deck.append(int(line))

    return p1_deck, p2_deck


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
