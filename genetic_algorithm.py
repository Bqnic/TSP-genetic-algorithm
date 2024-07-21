from case.city_positions import get_cities
from util.Chromosome import Chromosome
from util.natural_selection import pick_parents
import random

#chromosomes (solutions) are constructed in a way that the traversal is going through cities in order that is in the chromosome.
#initial population will just be cities array shuffled

cities = get_cities()

INITIAL_POPULATION_SIZE = 10

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

#picking parents
parent1, parent2 = pick_parents(population)


print("INITIAL POPULATION")
for chromosome in population:
    print(chromosome.__str__())

print(parent1, parent2)






