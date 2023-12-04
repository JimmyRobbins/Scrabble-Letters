import words
import spelling
import tiles

import string
import itertools

all_tiles = tuple((
    (letter1, letter2)
      for letter1 in string.ascii_uppercase 
      for letter2 in string.ascii_uppercase))

all_two_tiles = (
    (tile1, tile2) 
    for tile1 in all_tiles 
    for tile2 in all_tiles)

all_three_tiles = (
    (tile1, tile2, tile3)
    for tile1 in all_tiles
    for tile2 in all_tiles
    for tile3 in all_tiles
)

def all_n_tiles(n):
    return itertools.product(all_tiles, repeat=n)

word_list = words.custom_words


def test(tileset=all_n_tiles(2)):
    for n_tiles in tileset:
        failed = False
        if failed:
            failed = False
            continue
        for w in word_list:
            if not spelling.can_be_spelled(w, tiles.EXISTING_TILES + n_tiles):
                failed = True
                break
        if failed == False:
            return two_tiles
    return False

test()
