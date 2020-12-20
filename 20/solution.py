# fmt: off
import sys
from itertools import chain
from math import prod
from typing import List, Set, Iterable

sys.path.append("..")


# fmt: on


def part_1(tiles):
    # find edges
    edges = []

    for tile in tiles:
        neighbors = tile.find_neighbors(tiles)
        # print(tile.tile_id, neighbors)
        if len(neighbors) == 2:
            edges.append(tile)

    return prod(map(lambda t: t.tile_id, edges))


def part_2(tiles):
    # find edge
    for edge in tiles:
        neighbors = edge.find_neighbors(tiles)
        if len(neighbors) == 2:
            break
    else:
        edge = None

    # Turn edge to be the top left -> ?! does this work
    for r in range(4):
        top_left = edge.rotate(r)
        top, right, bottom, left = top_left.trbl_neighbors(tiles)
        if right and bottom:
            break
    else:
        raise Exception("Something went wrong!")

    top_left = top_left.flip_y().rotate()
    top_left.debug()

    # build image
    free_tiles = {tile.tile_id: tile for tile in tiles}

    image_tiles = []
    row = [top_left]
    next_tile: Tile = top_left
    del free_tiles[next_tile.tile_id]
    print(f"{next_tile} ", end="")

    while next_tile:
        # test available tiles
        right_tile = next_tile.find_neighbor(free_tiles.values(), "right")

        if right_tile:  # move right
            print(f" -> {right_tile}", end="")
            del free_tiles[right_tile.tile_id]
            row.append(right_tile)
            next_tile = right_tile
        else:  # end of row
            image_tiles.append(row)

            # search next tile below first in row
            next_tile = row[0].find_neighbor(free_tiles.values(), "bottom")
            print()
            print(f"{next_tile} ", end="")

            if next_tile:
                # add row to image
                row = [next_tile]
                del free_tiles[next_tile.tile_id]

    # crop and assemble image
    image_lines = []
    for row in image_tiles:
        in_row = [tile.crop() for tile in row]
        for lines in zip(*in_row):
            image_lines.append("".join(chain(*lines)))

    # search monsters
    # | .#...#.###...#.##.O#..
    # | O.##.OO#.#.OO.##.OOO##
    # | #O.#O#.O##O..O.#O##.##
    def monster_shape(x, y):
        """
        returns lookup data for monster shape at pos x, y
        """
        return {
            (x + 18, y + 0),
            (x + 0, y + 1),
            (x + 5, y + 1),
            (x + 6, y + 1),
            (x + 11, y + 1),
            (x + 12, y + 1),
            (x + 17, y + 1),
            (x + 18, y + 1),
            (x + 19, y + 1),
            (x + 1, y + 2),
            (x + 4, y + 2),
            (x + 7, y + 2),
            (x + 10, y + 2),
            (x + 13, y + 2),
            (x + 16, y + 2),
        }

    image_tile = Tile(0, image_lines)
    image_tile.debug()

    for image_tile in image_tile.permutate():
        debug = image_tile.top() == ".####...#####..#...###.."
        if debug:
            print("example:")

        # convert image to lookup
        image = set()
        roughness = 0
        for y, row in enumerate(image_tile.lines):
            for x, cell in enumerate(row):
                if cell == "#":
                    if debug:
                        print("add", f"({x}, {y})")
                    image.add((x, y))
                    roughness += 1

        monsters = 0
        for y, row in enumerate(image_tile.lines):
            for x, _ in enumerate(row):
                if monster_shape(x, y).issubset(image):
                    monsters += 1

        if monsters >= 1:
            if debug:
                print("example:")
                print("monsters:", monsters)
                print("roughness:", roughness - 15 * monsters)
            return roughness - 15 * monsters


class Tile:
    def __init__(self, tile_id, lines: List[str], degree=0):
        self.tile_id = int(tile_id)
        self.lines = lines
        self.degree = degree

    def debug(self):
        print()
        print("Tile: ", self.tile_id, "r:", self.degree)
        for row in self.lines:
            print(row)
        print()

    @staticmethod
    def from_input(lines):
        tile_id = lines.pop(0).replace("Tile ", "")[:-1]
        tile_lines = []
        while lines and (line := lines.pop(0)):
            tile_lines.append(line)

        return Tile(tile_id, tile_lines)

    def _rotate(self):
        """rotate clockwise"""
        lines = ["".join(reversed(c)) for c in zip(*self.lines)]
        degree = (self.degree + 90) % 360
        return Tile(self.tile_id, lines, degree=degree)

    def rotate(self, times=1):
        tile = self
        for _ in range(times):
            tile = tile._rotate()
        return tile

    def flip_x(self):
        return Tile(self.tile_id, lines=[line[::-1] for line in self.lines])

    def flip_y(self):
        return Tile(self.tile_id, list(reversed(self.lines)))

    def top(self) -> str:
        return self.lines[0]

    def bottom(self) -> str:
        return self.lines[-1]

    def left(self) -> str:
        return "".join([row[0] for row in self.lines])

    def right(self) -> str:
        return "".join([row[-1] for row in self.lines])

    def borders(self) -> Set[str]:
        return {
            self.top(),
            self.bottom(),
            self.left(),
            self.right(),
        }

    def find_neighbors(self, tiles):
        return [n for n in self.trbl_neighbors(tiles) if n]

    def trbl_neighbors(self, tiles):
        return (
            self.find_neighbor(tiles, "top"),
            self.find_neighbor(tiles, "right"),
            self.find_neighbor(tiles, "bottom"),
            self.find_neighbor(tiles, "left"),
        )

    def find_neighbor(self, tiles: Iterable["Tile"], dir: str):
        dirs = {
            "left": "right",
            "right": "left",
            "bottom": "top",
            "top": "bottom",
        }
        contra = dirs[dir]

        border = getattr(self, dir)()
        for tile in tiles:
            if self.tile_id == tile.tile_id:
                continue

            for tile in tile.permutate():
                if border == getattr(tile, contra)():
                    return tile

        return None

    def permutate(self):
        """
        yields all different orientations (incl x & y flip)
        """
        for r in range(4):
            yield self.rotate(r)

        x_tile = self.flip_x()
        for r in range(4):
            yield x_tile.rotate(r)

        y_tile = self.flip_y()
        for r in range(4):
            yield y_tile.rotate(r)

    def crop(self):
        return [line[1:-1] for line in self.lines[1:-1]]

    def __repr__(self):
        return f"<Tile {self.tile_id}>"


def parse(lines):
    tiles = []
    while lines:
        tiles.append(Tile.from_input(lines))

    return tiles


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(parse(lines[:])))
    print("Part 2: ", part_2(parse(lines[:])), "should not be 2556")


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
