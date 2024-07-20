from case import city_positions
import random

#chromosomes (solutions) are constructed in a way that the traversal is going through cities in order that is in the chromosome.
#initial population will just be cities array shuffled

cities = city_positions.get_cities()

INITIAL_POPULATION_SIZE = 7

initial_population = []

for i in range(0, INITIAL_POPULATION_SIZE):
    chromosome = cities.copy()
    random.shuffle(chromosome)
    initial_population.append(chromosome)

