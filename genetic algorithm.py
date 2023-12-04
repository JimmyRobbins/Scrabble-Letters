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

best_so_far = (
 ('U', 'N'),
 ('Y', 'I'),
 ('K', 'B'),
 ('M', 'E'),
 ('B', 'R'),
 ('K', 'H'),
 ('I', 'B'),
 ('B', 'J'),
 ('V', 'V'),
 ('F', 'P'),
 ('U', 'G'),
 ('Q', 'S'),
 ('T', 'L'),
 ('P', 'O'),
 ('H', 'O'),
 ('D', 'M')
)

best_as_nums = numpy.array(list(ord(x) for y in best_so_far for x in y))


def tiles_numbers_to_letters(numbers_array):
    return tuple(
        (chr(int(numbers_array[i])), 
         chr(int(numbers_array[i+1]))) for i in range(0, len(numbers_array), 2))

# def fitness_func(ga_instance, solution, solution_idx):
#    return words.score_tileset(tiles_numbers_to_letters(function_inputs) + tiles.EXISTING_TILES)

def fitness_func(ga_instance, solution, solution_idx):
    return words.score_tileset(tiles_numbers_to_letters(solution) + tiles.EXISTING_TILES)

fitness_function = fitness_func

num_generations = 50
num_parents_mating = 4

sol_per_pop = 12
num_genes = len(function_inputs)
gene_type = int

init_range_low = 65
init_range_high = 90

parent_selection_type = "rank"
keep_parents = 4
keep_elitism = 0

crossover_type = "single_point"
crossover_probability = 0.5

mutation_type = "random"
mutation_percent_genes = 10
mutation_by_replacement = True

save_solutions = True
save_best_solutions = False

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       gene_space=numpy.arange(65, 90),
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_type=gene_type,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       keep_elitism=keep_elitism,
                       crossover_type=crossover_type,
                       crossover_probability=crossover_probability,
                       mutation_type=mutation_type,
                       mutation_by_replacement=mutation_by_replacement,
                       mutation_percent_genes=mutation_percent_genes,
                       save_solutions=save_solutions,
                       save_best_solutions=save_best_solutions)

def go():
    ga_instance.run()

def report():
    solution=ga_instance.best_solution()

    print(f"score: {solution[1]}, generation: {ga_instance.best_solution_generation}")
    print(f"tiles:")
    best = tiles_numbers_to_letters(solution[0])
    print(best)

    print("can spell...")
    print(
        sorted(words.words_with_tiles(tiles_numbers_to_letters(solution[0])),
        key=len,
        reverse=True)
        )
    
    failed_a_custom_word = False
    for w in words.custom_words:
        if not spelling.can_be_spelled(w, best + tiles.EXISTING_TILES):
            failed_a_custom_word = True
            print(f"Oh NO!!! I can't spell {w}")
    if failed_a_custom_word == False:
        print("I can spell all the custom words!")

    other_words_can_spell = 0
    for w in words.top_words:
        if spelling.can_be_spelled(w, best + tiles.EXISTING_TILES):
            other_words_can_spell += 1
    print(f"I can spell {other_words_can_spell} of the top 1000 words!")