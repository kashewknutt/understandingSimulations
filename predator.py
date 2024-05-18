
import random
import numpy as np
class Predator:
    def __init__(self,gender,age,environmentClassInstance):  #gender is boolean true->male  false->female
        self.gender=gender
        self.age=age
        self.environment=environmentClassInstance
        self.colour=[255, 0, 0]
        self.x = random.randint(0, self.environment.dimension - 1)     #remember to check if the cell is empty first
        self.y = random.randint(0, self.environment.dimension - 1)
        self.environment.space[self.x,self.y] = self.colour     #predator is red
        self.energy=200     #initialised energy to 50 at the start
        self.enerygyForMovement=5
        self.attackEnergy=50  #energy increased for consuming blob(if you're feeling brave, give it the energy of the blob somehow)
        self.environment.predators.append(self)
    
    
    def movement(self):
        if(self.energy<=0):
            self.environment.predators.remove(self)
            self.environment.space[self.x,self.y]=[0,0,0]                                        #incase of death
            return

        self.environment.space[self.x, self.y] = [0, 0, 0]
        
        possible_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        random.shuffle(possible_moves)

        # checks for food/resource first so technically gives priority to it i gave it colour green: 0,200,0
        for move in possible_moves:
            new_x = self.x + move[0]
            new_y = self.y + move[1]
            if 0 <= new_x < self.environment.dimension and 0 <= new_y < self.environment.dimension:
                if np.array_equal(self.environment.space[new_x, new_y], [0, 0,150]):
                    self.attackBlob(new_x,new_y)
                    return

        # lets say agar resource doeesnt exist, toh itll automatically move to the available
        for move in possible_moves:
            new_x = self.x + move[0]
            new_y = self.y + move[1]
            if 0 <= new_x < self.environment.dimension and 0 <= new_y < self.environment.dimension:
                if np.array_equal(self.environment.space[new_x, new_y], [0, 0, 0]):
                    self.x, self.y = new_x, new_y
                    self.environment.space[self.x, self.y] = self.colour
                    self.energy-=self.enerygyForMovement
                    return

        # agar no empty it'll stay wahi; ab kuch nahi ho sakta in deadlock figure out karenge baadme what to do
        self.environment.space[self.x, self.y] = self.colour
    
    def attackBlob(self,x,y):
        self.x=x
        self.y=y
        self.environment.space[x,y]=self.colour
        self.energy+=self.attackEnergy
        self.energy-=self.enerygyForMovement