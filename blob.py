import random

class blob:
    def __init__(self, gender, age, environmentInstance):  #gender : true = male
        self.gender=gender
        self.age=age
        self.environement = environmentInstance
        x = random.randint(0, self.environment.dimension - 1)
        y = random.randint(0, self.environment.dimension - 1)
        self.environment.space[x,y] = [0, 0, 150]

    def movement(self):
        self.environment.space[self.x, self.y] = [0, 0, 0]
        possible_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        move = random.choice(possible_moves)

        new_x = (self.x + move[0]) % self.environment.dimension
        new_y = (self.y + move[1]) % self.environment.dimension
        self.x, self.y = new_x, new_y

        self.environment.space[self.x, self.y] = [0, 0, 150]

        