from case.city_positions import get_cities
from util.Chromosome import Chromosome
import random

#chromosomes (solutions) are constructed in a way that the traversal is going through cities in order that is in the chromosome.
#initial population will just be cities array shuffled

cities = get_cities()

INITIAL_POPULATION_SIZE = 7

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

#roulette selection
total_fitness = 0
for chromosome in population:
    total_fitness += chromosome.fitness_value

cum_sum = []
for i in range(0, len(population) - 1):
    sum = 0
    for j in range (i, len(population)):
        sum += population[j].fitness_value / total_fitness
    cum_sum.append(round(sum, 4))
cum_sum.append(0)

parent1 = 'x'
parent2 = 'x'
roulette_ball = random.uniform(0, 1)
for i in range(1, len(cum_sum)):
    if roulette_ball >= cum_sum[i]:
        parent1 = i - 1
        print(roulette_ball)
        print(parent1)
        break
roulette_ball = random.uniform(0, 1)
for i in range(1, len(cum_sum)):
    if roulette_ball >= cum_sum[i]:
        parent2 = i - 1
        print(roulette_ball)
        print(parent2)
        break

print("INITIAL POPULATION")
for chromosome in population:
    print(chromosome.__str__())

print(cum_sum)






