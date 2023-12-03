import tiles
import spelling
import string
import random
import numpy

all_tiles = ((ord(letter1), ord(letter2)) for letter1 in string.ascii_uppercase for letter2 in string.ascii_uppercase)

tiles_as_numbers = numpy.random.randint(65, 90, 32)

def tiles_numbers_to_letters(numbers_array):
    return tuple((chr(numbers_array[i]), chr(numbers_array[i+1])) for i in range(0, len(numbers_array), 2))

def fitness_func(ga_instance, solution, solution_idx):
    tiles_as_letters = (())