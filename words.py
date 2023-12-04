import csv
import spelling

words_and_values = ()

best_score = 0
best_words = []

# read custom words and points
with open('words.csv', mode='r') as words:
    reader = csv.reader(words)
    good_rows = (row for row in reader if len(row)==2)
    custom_words = {row[0]:int(row[1]) for row in good_rows}

#read top 1000 words and points
with open('1-1000.txt', mode='r') as top_1000:
    top_words = tuple(line.strip() for line in top_1000)



def score_tileset(tileset=()):
    score = 0
    spelled_words = []
    # test csutom words
    for word, value in custom_words.items():
        if spelling.can_be_spelled(word, tileset):
            score += value

    # test top 1000 words
    for word in top_words:
        if spelling.can_be_spelled(word, tileset):
            spelled_words.append(word)
            score += 1

    if score > best_score:
        best_words = spelled_words

    return score#, spelled_words

def words_with_tiles(tileset=()):
    score = 0
    spelled_words = []
    # test csutom words
    for word, value in custom_words.items():
        if spelling.can_be_spelled(word, tileset):
            spelled_words.append(word)
            score += value

    # test top 1000 words
    for word in top_words:
        if spelling.can_be_spelled(word, tileset):
            spelled_words.append(word)
            score += 1

    if score > best_score:
        best_words = spelled_words

    return spelled_words
