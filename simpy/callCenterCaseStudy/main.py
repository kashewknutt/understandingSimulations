import random
import simpy
import numpy as np

# Constants
maxEmployees = 10
avgTime = 5
callInterval = 2
simTime = 120
customersHandled = 0

class CallCenter:
    def __init__(self, env, numEmployees, supportTime):
        self.env = env
        self.staff = simpy.Resource(env, numEmployees)
        self.supportTime = supportTime

    def support(self, customer):
        randomTime = max(1, np.random.normal(self.supportTime, 4))
        yield self.env.timeout(randomTime)
        print(f"Support finished for {customer} at {self.env.now:.2f}")


def customer(env, name, callCenter):
    global customersHandled
    print(f"Call from {name} at {env.now:.2f}")
    with callCenter.staff.request() as request:
        yield request
        print(f"Call from {name} assigned to an employee at {env.now:.2f}")
        yield env.process(callCenter.support(name))
        print(f"Customer {name} left call at {env.now:.2f}")
        customersHandled += 1

def setup(env, numEmployees, avgTime, callInterval):
    callCenter = CallCenter(env, numEmployees, avgTime)

    for i in range(5):
        env.process(customer(env, i, callCenter))
    
    while True:
        yield env.timeout(random.expovariate(1.0 / callInterval))
        i += 1
        env.process(customer(env, i, callCenter))

if __name__ == "__main__":
    print("Starting Simulation")
    env = simpy.Environment()
    env.process(setup(env, maxEmployees, avgTime, callInterval))
    env.run(until=simTime)
    print(f"Simulation ended with {customersHandled} customers handled")