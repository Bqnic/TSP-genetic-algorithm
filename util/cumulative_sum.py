def find_cum_sum(population):
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

    return cum_sum