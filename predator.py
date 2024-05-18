
import random
class predator:
    def __init__(self,gender,age,environmentClassInstance):  #gender is boolean true->male  false->female
        self.gender=gender
        self.age=age
        self.environment=environmentClassInstance
        self.x = random.randint(0, self.environment.dimension - 1)
        self.y = random.randint(0, self.environment.dimension - 1)
        self.environment.space[self.x,self.y] = [255, 0, 0]     #predator is red
        self.energy=50     #initialised energy to 50 at the start
    
    
    
    def movement(self):
        xAdd=random.randint(-1,1)
        yAdd=random.randint(-1,1)
        newCoordinate=[self.x+xAdd,self.y+yAdd]
        if(self.environment.space[newCoordinate[0]][newCoordinate[1]]!=[0,0,0]):
            self.movement()
        self.environment.space[newCoordinate[0]][newCoordinate[1]]=[255,0,0]
        self.environment.space[self.x][self.y]=[0,0,0]
        self.x=newCoordinate[0]
        self.y=newCoordinate[1]