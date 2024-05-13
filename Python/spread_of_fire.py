import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def spread_of_fire(grid_size, burn_probability, experiment_number):
    burned_percentages = []
    for i in range(experiment_number):
        grid = [['Tree' for i in range(grid_size)] for j in range(grid_size)] # make every cell become tree in initialization
        grid[grid_size // 2][grid_size // 2] = 'Burning' # make the middle grid become burning

        changed = True # make loop run at least once
        while changed:
            changed = False
            for i in range(grid_size):
                for j in range(grid_size):
                    if grid[i][j] == 'Burning':
                        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # spread possibility using Von Neumann neighbourhood method
                            new_i, new_j = i + di, j + dj # new coordinate that possibly become burning
                            if 0 <= new_i < grid_size and 0 <= new_j < grid_size: # make sure the fire doesnot come out the grid
                                if grid[new_i][new_j] == 'Tree' and random.random() < burn_probability: # determine the new cell become burning or not depend on the random number and burn probability
                                     grid[new_i][new_j] = 'Burning'
                                     changed = True

        # calculate the burning area percentage
        burned_count = sum(cell == 'Burning' for row in grid for cell in row)
        burned_percentage = burned_count / (grid_size * grid_size) * 100
        burned_percentages.append(burned_percentage)

    return np.mean(burned_percentages)

def extract_data(burn_probabilities, experiment_number):
    burned_percentages = []
    for burn_probability in burn_probabilities:
        average_burned_percentage = spread_of_fire(grid_size, burn_probability, experiment_number)
        burned_percentages.append((burn_probability, average_burned_percentage))

    data = pd.DataFrame(burned_percentages, columns=["Burn Probability", "Average Burned Percentage"])
    return data

grid_size = 17
experiment_number = 10
burn_probabilities = np.arange(.1, 1., .1)

data = extract_data(burn_probabilities, experiment_number)

def logistic_function(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

# Set initial parameter values (informed guesses)
L_init = 100  # Maximum value
k_init = 5  # Growth rate
x0_init = 0.5  # Inflection point

# Perform curve fitting using Levenberg-Marquardt algorithm
popt, pcov = curve_fit(logistic_function, data["Burn Probability"], data["Average Burned Percentage"], p0=[L_init, k_init, x0_init], method='lm')
L, k, x0 = popt

# Plot data and fitted curve
plt.figure(figsize=(10, 6))
plt.plot(data["Burn Probability"], data["Average Burned Percentage"], marker='o', linestyle='-', label='Data')
plt.plot(data["Burn Probability"], logistic_function(data["Burn Probability"], *popt), label='Fitted Curve')
plt.xlabel("Burn Probability")
plt.ylabel("Average Burned Percentage")
plt.title("Fire Simulation Results")
plt.legend()
plt.grid(True)
plt.show()

# Print curve fitting parameters
print("Curve fitting parameters:")
print("L =", L)
print("k =", k)
print("x0 =", x0)