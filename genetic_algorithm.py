from case.city_positions import get_cities
from util.Chromosome import Chromosome
import random

#chromosomes (solutions) are constructed in a way that the traversal is going through cities in order that is in the chromosome.
#initial population will just be cities array shuffled

cities = get_cities()

INITIAL_POPULATION_SIZE = 7

initial_population = []

for i in range(0, INITIAL_POPULATION_SIZE):
    random_traversal_order = cities.copy()
    random.shuffle(random_traversal_order)
    chromosome = Chromosome(random_traversal_order)

    initial_population.append(chromosome)

#readjusting fitness values
min_fitness_value = initial_population[0].fitness_value
for chromosome in initial_population:
    if chromosome.fitness_value < min_fitness_value:
        min_fitness_value = chromosome.fitness_value

min_fitness_value = min_fitness_value - 1
for chromosome in initial_population:
    chromosome.fitness_value -= min_fitness_value 

print("INITIAL POPULATION")
for chromosome in initial_population:
    print(chromosome.__str__())



