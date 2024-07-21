import random
import numpy as np

def get_city_index(city, parent):
    ''' Helper function to find the index of a city in the parent array '''
    for i in range(len(parent)):
        if np.array_equal(parent[i], city):
            return i
    return -1

def pmx(parent1, parent2, child, crossover_point1, crossover_point2):
    '''
    partially mapped crossover(pmx)
    '''
    for i in range(len(parent1)):
        if i < crossover_point1 or i >= crossover_point2:
            candidate = parent2[i]
            while any(np.array_equal(candidate, city) for city in parent1[crossover_point1:crossover_point2]):
                index = get_city_index(candidate, parent1)
                candidate = parent2[index]
            child[i] = candidate
    return child

def recombine(parent1, parent2):
    #picking crossover points
    crossover_point1 = random.randint(0, len(parent1) - 1)
    crossover_point2 = random.randint(crossover_point1 + 1, len(parent1))

    #doing pmx
    child1 = parent1.copy()
    child2 = parent2.copy()

    child1 = pmx(parent1, parent2, child1, crossover_point1, crossover_point2)
    child2 = pmx(parent2, parent1, child2, crossover_point1, crossover_point2)

    return child1, child2

    
    