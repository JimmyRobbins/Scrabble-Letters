import random

EXISTING_TILES = (
    ("G", "V"),
    ("D", "O"),
    ("W", "F"),
    ("C", "I"),
    ("T", "E"),
    ("H", "Y"),
    ("R", "A"),
    ("N", "L"),
    ("K", "M"),
    ("S", "A")
)

def create_random_tile():
    return (chr(random.randint(ord('A'), ord('Z'))), chr(random.randint(ord('A'), ord('Z'))))

def create_random_tiles(how_many):
    return tuple(create_random_tile() for i in range(how_many))

