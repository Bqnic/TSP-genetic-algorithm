import random
import numpy as np

def recombine(parent1, parent2):
    '''
    partially mapped crossover(pmx)
    '''
    #picking crossover points
    crossover_point1 = random.randint(0, len(parent1) - 1)
    crossover_point2 = random.randint(crossover_point1 + 1, len(parent1))

    #doing pmx
    child1 = np.zeros((len(parent1), 2), dtype=int)
    child1[crossover_point1:crossover_point2] = parent1[crossover_point1:crossover_point2].copy()

    def get_city_index(city, parent):
        ''' Helper function to find the index of a city in the parent array '''
        for i in range(len(parent)):
            if np.array_equal(parent[i], city):
                return i
        return -1

    # Fill the remaining positions with the correct cities from parent2
    for i in range(len(parent1)):
        if i < crossover_point1 or i >= crossover_point2:
            candidate = parent2[i]
            while any(np.array_equal(candidate, city) for city in parent1[crossover_point1:crossover_point2]):
                index = get_city_index(candidate, parent1)
                candidate = parent2[index]
            child1[i] = candidate



    
    