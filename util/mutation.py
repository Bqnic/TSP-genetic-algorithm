import random

def mutate(traversal):
    #picking crossover points
    crossover_point1 = random.randint(0, len(traversal) - 2)
    crossover_point2 = random.randint(crossover_point1 + 1, len(traversal) - 1)

    #mutating
    while crossover_point2 > crossover_point1:
        traversal[crossover_point2], traversal[crossover_point1] = traversal[crossover_point1], traversal[crossover_point2]
        crossover_point2 -= 1
        crossover_point1 += 1