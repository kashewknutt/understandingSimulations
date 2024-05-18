from environment import Environment
from predator import Predator
from blob import blob

env=Environment(50)
predators = [Predator(True, 5, env) for _ in range(10)]
