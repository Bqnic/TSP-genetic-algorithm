from case.city_positions import get_cities
from util.Chromosome import Chromosome
from util.natural_selection import pick_parents
from util.recombination import recombine
from util.mutation import mutate
import random

#chromosomes (solutions) are constructed in a way that the traversal is going through cities in order that is in the chromosome.
#initial population will just be cities array shuffled

cities = get_cities()

INITIAL_POPULATION_SIZE = 10
MUTATION_PROBABILITY = 0.05

population = []

for i in range(0, INITIAL_POPULATION_SIZE):
    random_traversal_order = cities.copy()
    random.shuffle(random_traversal_order)
    chromosome = Chromosome(random_traversal_order)

    population.append(chromosome)

#readjusting fitness values to be > 0
min_fitness_value = population[0].fitness_value
for chromosome in population:
    if chromosome.fitness_value < min_fitness_value:
        min_fitness_value = chromosome.fitness_value

min_fitness_value = min_fitness_value - 1
for chromosome in population:
    chromosome.fitness_value -= min_fitness_value 

#sorting chromosomes in population according to their fitness value
population.sort(key=lambda chromosome: chromosome.fitness_value, reverse=True)

print("INITIAL POPULATION")
for chromosome in population:
    print(chromosome.__str__())

#picking parents
parent1, parent2 = pick_parents(population)

#recombination
recombine(parent1.traversal, parent2.traversal)

#mutation
for chromosome in population:
    mutation_roll = random.uniform(0, 1)
    if mutation_roll < MUTATION_PROBABILITY:
        mutate(chromosome.traversal)
        print("MUTATED CHROMOSOME")
        print(chromosome)





