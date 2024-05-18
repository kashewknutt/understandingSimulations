from environment import Environment
from predator import Predator
from blob import Blob
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

env=Environment(50)
predators = [Predator(True, 5, env) for _ in range(10)]
blobs=[Blob(True, 5, env) for _ in range(10)]
def update(frame):                            #decrement age after you add the die function for all entities
    for obj in env.blobs:
        if obj is None:
            .remove(obj)
    for blob in blobs:
        blob.movement()  
    for predator in predators:
        predator.movement()  
    # Update the plot
    im.set_array(env.space)
    return [im]
fig, ax = plt.subplots()
im = ax.imshow(env.space, animated=True)

ani = animation.FuncAnimation(fig, update, frames=200, interval=100, blit=True) #actually animates all the frames
plt.show()