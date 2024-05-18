import numpy as np


class Graph:
    def __init__(self, dimension, blobs, predators):
        self.dimension = dimension
        self.blobs = blobs
        self.predators = predators
        self.space = np.zeros(dimension, dimension, blobs, predators)