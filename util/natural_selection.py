import random

def pick_parents(population, cum_sum):
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