import random

def pick_parents(population):
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
            parent2 = i - 1
            break

    while parent1 == parent2:
        roulette_ball = random.uniform(0, 1)
        for i in range(1, len(cum_sum)):
            if roulette_ball >= cum_sum[i]:
                parent2 = i - 1
                break

    return population[parent1], population[parent2]