import numpy as np

class Environment:
    def __init__(self, dimension):
        self.dimension = dimension
        # Initialize a 3D numpy array with zeros. Each pixel has 3 values (R, G, B).
        self.space = np.zeros((dimension, dimension, 3), dtype=int)