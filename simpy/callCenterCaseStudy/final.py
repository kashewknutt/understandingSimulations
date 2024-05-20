import main
import matplotlib.pyplot as plt

# Number of times to run the sim
n = 100

# Customers handled array
customershandled = []

# Run the simulation 10 times
for i in range(n):
    customershandled.append(main.simulate())

# Plot the customers handled array using matplotlib
plt.plot(customershandled, label='Customers')
plt.show()