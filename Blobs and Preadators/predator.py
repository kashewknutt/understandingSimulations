
import random
import numpy as np
import simpleaudio as sa

class Predator:
    def __init__(self,gender,age,environmentClassInstance,x=-1,y=-1):  #gender is boolean true->male  false->female
        self.gender=gender
        self.age=age
        self.environment=environmentClassInstance
        male=[255,0,0]
        female=[255, 105, 97]
        if self.gender:
            self.colour=male
        else:
            self.colour=female
        if(x==-1):
            self.x = random.randint(0, self.environment.dimension - 1)     #remember to check if the cell is empty first
            self.y = random.randint(0, self.environment.dimension - 1)
        else:
            self.x=x
            self.y=y
        self.environment.space[self.x,self.y] = self.colour     #predator is red
        self.energy=200     #initialised energy to 50 at the start
        self.enerygyForMovement=10
        self.attackEnergy=50  #energy increased for consuming blob(if you're feeling brave, give it the energy of the blob somehow)
        self.environment.predators.append(self)
    
    
    def movement(self):
        if(self.energy<=0 or self.age>50):                 #incase of death
            self.environment.predators.remove(self)
            self.environment.space[self.x,self.y]=[0,0,0]   
            del(self)                                      #releasing memory from the heap
            return

        self.sex()                          #sex                   
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

    def sex(self):           #when sexually active mates meet 
        if self.gender==False and self.age>=20 and self.energy>=400:
            for i in range(-1,2):
                for j in range(-1,2):
                    new_x = self.x + i
                    new_y = self.y + j
                    if 0 <= new_x < self.environment.dimension and 0 <= new_y < self.environment.dimension:
                        if np.array_equal(self.environment.space[new_x, new_y], [255, 0, 0]):
                            for p in range(-1,2):
                                for q in range(-1,2):
                                    x_child = self.x + p
                                    y_child = self.y + q
                                    if 0 <= x_child < self.environment.dimension and 0 <= y_child < self.environment.dimension:
                                        if np.array_equal(self.environment.space[x_child,y_child], [0, 0, 0]):
                                            rand=random.choice([True, False])
                                            Predator(rand,5,self.environment,x_child,y_child)
                                            #wave_obj = sa.WaveObject.from_wave_file('button-2.wav')

                                            # Stop any currently playing sound
                                            #sa.stop_all()

                                            # Play the new sound
                                            #play_obj = wave_obj.play()
                                            print("reproduction happened")
                                            return

