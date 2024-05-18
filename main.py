from environment import Environment
from graph import Graph
from predator import Predator
from blob import Blob
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
blob_number_per_frame=[]
predator_number_per_frame=[]
env=Environment(50)
for _ in range(20):
    Predator(True, 5, env)
for _ in range(50):
    Blob(True, 5, env)
def update(frame):                           #decrement age after you add the die function for all entities
    #print(env.blobs)
    for blob in env.blobs:
        blob.age -= 0.2
        blob.movement()
    for predator in env.predators:
        predator.age -= 0.2
        #print(predator)
        predator.movement()  
    # Update the plot
    im.set_array(env.space)
    blob_number_per_frame.append(len(env.blobs))
    predator_number_per_frame.append(len(env.predators))
    return [im]
fig, ax = plt.subplots()
im = ax.imshow(env.space, animated=True)
ani = animation.FuncAnimation(fig, update, frames=200, interval=100, blit=True) #actually animates all the frames
plt.show()

plt.plot(blob_number_per_frame, label='Blobs')
plt.plot(predator_number_per_frame, label='Predators')
plt.xlabel('Frame')
plt.ylabel('Number of entities')
plt.show()