import random

import numpy as np

class blob:
    def __init__(self, gender, age, environmentInstance):  #gender : true = male
        self.gender=gender
        self.age=age
        self.environment = environmentInstance
        self.energy = 50
        self.x = random.randint(0, self.environment.dimension - 1)
        self.y = random.randint(0, self.environment.dimension - 1)
        self.environment.space[self.x,self.y] = [0, 0, 150]
        self.energy_for_movement = 10
        self.food_content = 30

    def movement(self):
        self.environment.space[self.x, self.y] = [0, 0, 0]
        
        possible_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        random.shuffle(possible_moves)


        #RESOURCE CONSUMPTION
        # checks for food/resource first so technically gives priority to it i gave it colour green: 0,200,0
        for move in possible_moves:
            new_x = self.x + move[0]
            new_y = self.y + move[1]
            if 0 <= new_x < self.environment.dimension and 0 <= new_y < self.environment.dimension:
                if np.array_equal(self.environment.space[new_x, new_y], [0, 200, 0]):
                    self.x, self.y = new_x, new_y
                    self.environment.space[self.x, self.y] = [0, 0, 150]
                    self.energy += self.food_content
                    self.energy -= self.energy_for_movement
                    return

        # lets say agar resource doeesnt exist, toh itll automatically move to the available
        for move in possible_moves:
            new_x = self.x + move[0]
            new_y = self.y + move[1]
            if 0 <= new_x < self.environment.dimension and 0 <= new_y < self.environment.dimension:
                if np.array_equal(self.environment.space[new_x, new_y], [0, 0, 0]):
                    self.x, self.y = new_x, new_y
                    self.environment.space[self.x, self.y] = [0, 0, 150]
                    self.energy -= self.energy_for_movement
                    return

        # agar no empty it'll stay wahi; ab kuch nahi ho sakta in deadlock figure out karenge baadme what to do
        self.environment.space[self.x, self.y] = [0, 0, 150]


        