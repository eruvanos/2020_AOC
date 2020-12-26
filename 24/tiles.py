import re
from collections import Counter

from utils.vector import Vector

PATTERN = re.compile(r"(ne|se|sw|nw|e|w)")

E = "e"
SE = "se"
SW = "sw"
W = "w"
NW = "nw"
NE = "ne"

MOVES = {
    E: Vector(1, 0),
    SE: Vector(1, -1),
    NE: Vector(0, 1),
    W: Vector(-1, 0),
    SW: Vector(0, -1),
    NW: Vector(-1, 1),
}


class Grid:
    def __init__(self):
        self.tiles = set()

    @staticmethod
    def walk(seq: str):
        cur = Vector(0, 0)
        for dir in PATTERN.findall(seq):
            cur = cur + MOVES[dir]

        return cur

    def get(self, pos: Vector):
        return pos in self.tiles

    def flip(self, pos: Vector):
        if pos in self.tiles:
            self.tiles.remove(pos)
        else:
            self.tiles.add(pos)

    def walk_and_flip(self, seq: str, debug=False):
        pos = Grid.walk(seq)
        self.flip(pos)
        if debug:
            print(f"Flip {pos} to {self.tiles[pos]}")

        return self

    @staticmethod
    def neighbors(pos):
        return [pos + off for off in MOVES.values()]


def simulate(state):
    new_state = set()
    all_neighbors = Counter()

    # calc active cells
    for tile in state:
        ns = Grid.neighbors(tile)

        for n in ns:
            all_neighbors[n] += 1

        active_ns = len(state.intersection(ns))
        if active_ns in (1, 2):
            new_state.add(tile)

    # spawn new cells
    for tile in all_neighbors.keys() - state:
        if all_neighbors[tile] == 2:
            new_state.add(tile)

    return new_state
