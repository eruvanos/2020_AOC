from math import sqrt
from pathlib import Path
from typing import List

import arcade
from arcade import (
    Window,
    View,
    ShapeElementList,
    create_rectangle_filled,
    create_rectangle_outline,
)
from arcade.color import WHITE, BLACK, RED

import solution
from solution import Tile

PIXEL = 10
TILE_SIZE = PIXEL * 11


class TileView(View):
    def __init__(self, tiles: List[Tile]):
        super().__init__()
        self.tiles = tiles

        self.shapes = self.generate_shapes()

    def on_show_view(self):
        arcade.set_background_color(BLACK)

    def generate_shapes(self):
        size = sqrt(len(self.tiles))

        shapes = []
        for i, tile in enumerate(self.tiles):
            tx = i % size
            ty = i // size

            cx = TILE_SIZE + tx * TILE_SIZE
            cy = TILE_SIZE + ty * TILE_SIZE

            shape = ShapeElementList()
            for y, row in enumerate(reversed(tile.lines)):
                for x, pxl in enumerate(row):
                    if pxl == "#":
                        shape.append(
                            create_rectangle_filled(
                                cx + x * PIXEL,
                                cy + y * PIXEL,
                                PIXEL,
                                PIXEL,
                                color=WHITE,
                            )
                        )
            shapes.append(shape)

            # Add border
            print(shape.center_x, shape.center_y)
            rect = create_rectangle_outline(
                shape.center_x,
                shape.center_y,
                len(tile.lines) * PIXEL,
                len(tile.lines) * PIXEL,
                RED,
                # border_width=1,
            )
            shapes.append(rect)

        return shapes

    def on_draw(self):
        arcade.start_render()
        for shape in self.shapes:
            shape.draw()


if __name__ == "__main__":
    lines = Path("test_input.txt").read_text().splitlines()
    tiles = solution.parse(lines)

    win = Window()
    win.show_view(TileView(tiles))

    arcade.run()
