from utils.vector import Vector

# Directions
NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"

# Vectors for NESW
NESW_VEC = {
    "E": Vector(1, 0),
    "W": Vector(-1, 0),
    "N": Vector(0, 1),
    "S": Vector(0, -1),
}

# Turn maps for NESW
TURN_LEFT = {
    "E": "N",
    "W": "S",
    "N": "W",
    "S": "E",
}
TURN_RIGHT = {
    "E": "S",
    "W": "N",
    "N": "E",
    "S": "W",
}

# ARROW directions
UDRL_VEC = {
    "U": Vector(0, 1),
    "D": Vector(0, -1),
    "R": Vector(1, 0),
    "L": Vector(-1, 0),
}


NESW_ARROW = {
    "E": "R",
    "W": "L",
    "N": "U",
    "S": "D",
}
"""Convert NESW to Arrow"""

ARROW_NESW = {
    "R": "E",
    "L": "W",
    "U": "N",
    "D": "S",
}
"""Convert Arrow to NESW"""

ANGLES_DIR = {"R": 90, "L": 270, "U": 0, "D": 180}
"""ARROW to Angle U = 0° """
