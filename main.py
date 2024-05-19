from environment import Environment
from graph import Graph
from predator import Predator
from blob import Blob
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

#array that will store numbers per frame of entities for analyzing graph
blob_number_per_frame=[]
predator_number_per_frame=[]

#constants
maxPredators = 20
maxBlobs = 20
maxFrames = 200

#Simulation Environment
env=Environment(50)

#selecting random frames for the predators to spawn
predFrames = [random.randint(0,maxFrames) for _ in range(maxPredators)]
predFrames.sort()
#selecting random frames for the blobs to spawn
blobFrames = [random.randint(0,maxFrames) for _ in range(maxBlobs)]
blobFrames.sort()

#increment age after you add the die function for all entities
def update(frame):
    #print(env.blobs)

    #generating 5 blobs at random frames
    if frame in blobFrames:
        for _ in range(5):
            tempForGender=random.choice([True, False])
            Blob(tempForGender, 5, env)

    #Blob movement in each frame
    for blob in env.blobs:
        blob.age += 0.2
        blob.movement()


    #Predator generating in random frames
    if frame in predFrames:
        tempForGender=random.choice([True, False])
        Predator(tempForGender, 5, env)
    

    #Predator movement in each frame
    for predator in env.predators:
        predator.age += 0.2
        #print(predator)
        predator.movement()

    #generate food every 10 frames
    if frame%10==0 and frame != 0:
        env.add_food([],5,10)
 
    # Update the plot
    im.set_array(env.space)
    blob_number_per_frame.append(len(env.blobs))
    predator_number_per_frame.append(len(env.predators))
    return [im]

#plotting the graph
fig, ax = plt.subplots()
im = ax.imshow(env.space, animated=True)
ani = animation.FuncAnimation(fig, update, frames=maxFrames, interval=100, blit=True) #actually animates all the frames
plt.show()

plt.plot(blob_number_per_frame, label='Blobs')
plt.plot(predator_number_per_frame, label='Predators')
plt.xlabel('Frame')
plt.ylabel('Number of entities')
plt.show()