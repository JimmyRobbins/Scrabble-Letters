

existing_tiles = (
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

# Currently greedy (always takes first matching tile)
# How can I account for duplicate letters?

def can_be_spelled(word, tiles=()):

    # use existing_tiles if available_tiles isn't specified
    if tiles == ():
        available_tiles=list(existing_tiles)
    else:
        available_tiles=list(tiles)

    # use i to generate subwords for recursively testing tile options
    for i, letter in enumerate(word):
        candidate_tiles = []

        for tile in available_tiles:
            if tile[0] == letter or tile[1] == letter:
                candidate_tiles.append(tile)

        if len(candidate_tiles) == 0:
            # needed letter isn't on available tiles
            return False
        
        elif len(candidate_tiles) == 1:
            # there's only one possible tile
            available_tiles.remove(candidate_tiles[0])
            continue # jump to the next letter

        else: 
        # more than one tile has the letter
            remaining_word = word[i+1:]
            for candidate_tile in candidate_tiles:
                available_tiles.remove(candidate_tile)
                if can_be_spelled(remaining_word, tuple(available_tiles)):
                    return True
                # can't continue with that tile...
                # put the tile back in the pile & try the next one
                available_tiles.append(candidate_tile)

    return True

can_be_spelled("FAMILY")

can_be_spelled("OOX", (("O", "B"), ("O", "X"), ("A", "O")))

can_be_spelled("OXX", (("O", "B"), ("O", "X"), ("A", "O")))