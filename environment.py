import numpy as np

class Environment:
    def __init__(self, dimension):
        self.dimension = dimension
        self.space = np.zeros((dimension, dimension, 3), dtype=int)