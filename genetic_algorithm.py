from case.city_positions import get_cities
from util.Chromosome import Chromosome
from util.natural_selection import pick_parents
from util.recombination import recombine
from util.mutation import mutate
from util.cumulative_sum import find_cum_sum
import random

#chromosomes (solutions) are constructed in a way that the traversal is going through cities in order that is in the chromosome.
#initial population will just be cities array shuffled

cities = get_cities()

INITIAL_POPULATION_SIZE = 80
MUTATION_PROBABILITY = 0.08
NUMBER_OF_GENERATIONS = 120
PERCENTAGE_OF_ELITES = 0.1

#inserting initial population
population = []

for i in range(0, INITIAL_POPULATION_SIZE):
    random_traversal_order = cities.copy()
    random.shuffle(random_traversal_order)
    chromosome = Chromosome(random_traversal_order)

    population.append(chromosome)

for generation in range (1, NUMBER_OF_GENERATIONS + 1): 
    #sorting chromosomes in population according to their fitness value
    population.sort(key=lambda chromosome: chromosome.fitness_value)

    print(f"BEST FROM GENERATION {generation}: ")
    print(population[0])

    new_population = []

    #finding cumulative sum for the roulette selection
    cum_sum = find_cum_sum(population)
    
    #recombination
    for i in range(0, (5 * generation) + INITIAL_POPULATION_SIZE):
        parent1, parent2 = pick_parents(population, cum_sum)
        child1, child2 = recombine(parent1.traversal, parent2.traversal)
        new_population.append(Chromosome(child1))
        new_population.append(Chromosome(child2))

    #mutation
    for chromosome in new_population:
        mutation_roll = random.uniform(0, 1)
        if mutation_roll < MUTATION_PROBABILITY:
            mutate(chromosome.traversal)

    #elitism
    for i in range(0, round(PERCENTAGE_OF_ELITES * len(population))):
        new_population.append(Chromosome(population[i].traversal))

    population = new_population




