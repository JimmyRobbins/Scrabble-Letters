import csv
import spelling

words_and_values = ()

with open('words.csv', mode='r') as words:
    reader = csv.reader(words)
    good_rows = (row for row in reader if len(row)==2)
    words_and_values = {row[0]:int(row[1]) for row in good_rows}

def score_tileset(tileset=()):
    score = 0
    for word, value in words_and_values.items():
        print(f"testing {word}")
        if spelling.can_be_spelled(word, tileset):
            print(f"spelled {word} for {value} points")
            score += value
    return score
