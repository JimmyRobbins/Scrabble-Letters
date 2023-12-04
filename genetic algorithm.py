import tiles
import spelling
import words

import pygad

import string
import random
import numpy

function_inputs = numpy.random.randint(65, 90, 32)
starter_tiles =(
    ("C", "R"),
    ("H", "O"),
    ("R", "B"),
    ("I", "B"),
    ("S", "I"),
    ("T", "N"),
    ("M", "S"),
    ("A", "I"),
    ("S", "T"),
    ("F", "H"),
    ("I", "D"),
    ("E", "Y"),
    ("L", "P"),
    ("L", "M"),
    ("H", "M"),
)

best_so_far = (('U', 'N'), ('D', 'P'), ('Y', 'N'), ('O', 'S'), ('S', 'U'), ('I', 'F'), ('J', 'D'), ('I', 'E'), ('R', 'W'), ('D', 'I'), ('R', 'M'), ('K', 'X'), ('H', 'R'), ('C', 'D'), ('B', 'I'))

# function_inputs = numpy.array(list(ord(x) for y in best_so_far for x in y))

desired_output = 1000000

def tiles_numbers_to_letters(numbers_array):
    return tuple(
        (chr(int(numbers_array[i])), 
         chr(int(numbers_array[i+1]))) for i in range(0, len(numbers_array), 2))

def fitness_func(ga_instance, solution, solution_idx):
    return words.score_tileset(tiles_numbers_to_letters(function_inputs) + tiles.EXISTING_TILES)

fitness_function = fitness_func

num_generations = 50
num_parents_mating = 4

sol_per_pop = 12
num_genes = len(function_inputs)
gene_type = int

init_range_low = -2
init_range_high = 5

parent_selection_type = "sss"
keep_parents = -1
keep_elitism = 4

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       gene_space=range(65, 90),
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_type=gene_type,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       keep_elitism=keep_elitism,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

def go():
    ga_instance.run()

def report():
    solution=ga_instance.best_solution()

    print(f"score: {solution[1]}, generation: {solution[2]}")
    print(f"tiles:")
    best = tiles_numbers_to_letters(solution[0])
    print(best)

    print("can spell...")
    print(
        sorted(words.words_with_tiles(tiles_numbers_to_letters(solution[0])),
        key=len,
        reverse=True)
        )

    for w in words.custom_words:
        if not spelling.can_be_spelled(w, best + tiles.EXISTING_TILES):
            print(f"Oh NO!!! I can't spell {w}")