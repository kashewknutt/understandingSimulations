from environment import environment
import random
class predator:
    def __init(self,gender,age,environmentClassInstance):  #gender is boolean true->male  false->female
        self.gender=gender
        self.age=age
        self.environment=environmentClassInstance
        x = random.randint(0, self.environment.dimension - 1)
        y = random.randint(0, self.environment.dimension - 1)
        self.environment.space[x,y] = [255, 0, 0]     #predator is red
