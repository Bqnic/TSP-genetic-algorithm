import math

class Chromosome:
    def __init__(self, traversal):
        self.traversal = traversal
        self.fitness_value = self.calculate_fitness()

    def __str__(self):
        return f"{self.traversal}, fitness value = {self.fitness_value}"
    
    def calculate_fitness(self):
        #fitness function is calculated as 1 / Euclidean distance
        distance = 0
        for i in range(0, len(self.traversal) - 1):
            distance += math.sqrt(
                        math.pow(self.traversal[i][0] - self.traversal[i + 1][0], 2) +
                        math.pow(self.traversal[i][1] - self.traversal[i + 1][1], 2))
            
        return 1 / distance