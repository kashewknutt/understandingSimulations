#Simulating and plotting projectiles with random initial velocities and angle of inclination

import numpy as np
import matplotlib.pyplot as plt


def projectile_motion(v0, angle_deg, num_points=500):


    #apparantly np doesn't do degrees
    angle_rad = np.radians(angle_deg)
    
    # Initial velocities
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)
    
    t_flight = 2 * v0 * np.sin(angle_rad) / 9.81
    
    t = np.linspace(0, t_flight, num_points)
    
    # Calculate positions
    x = v0x * t
    y = v0y * t - 0.5 * 9.81 * t**2

    #print(x,y)
    
    return x, y

def simulate(num_points=500):
    v0 = np.random.uniform(10, 100)
    angle = np.random.uniform(0, 90)
    x, y = projectile_motion(v0, angle, num_points)
    return x,y


n = 100
runs = []
for i in range(n):
    x,y = simulate()
    plt.plot(x, y, label='Projectile Motion')
plt.show()