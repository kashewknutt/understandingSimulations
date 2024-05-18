import random
import numpy as np

class Environment:
    def __init__(self, dimension):
        self.dimension = dimension
        self.space = np.zeros((dimension, dimension, 3), dtype=int)
        self.add_food()
        self.blobs=[]
        self.predators=[]

    
    # food is added. food_position list of fixed food positions, if any [(x1, y1), (x2, y2)]; percentage = limits percentage of screen to be food
    def add_food(self, food_positions=[], min_food_percentage=5, max_food_percentage=10):
        
        if food_positions:
            for pos in food_positions:
                if 0 <= pos[0] < self.dimension and 0 <= pos[1] < self.dimension:
                    self.space[pos[0], pos[1]] = [0, 200, 0]

        food_percentage = random.randint(min_food_percentage, max_food_percentage)
        min_num_random_food = int((food_percentage / 100) * (self.dimension ** 2))

        num_random_food = max(min_num_random_food - len(food_positions), 0)
        for _ in range(num_random_food):
            x = random.randint(0, self.dimension - 1)
            y = random.randint(0, self.dimension - 1)
            if np.array_equal(self.space[x, y], [0, 0, 0]):
                self.space[x, y] = [0, 200, 0]