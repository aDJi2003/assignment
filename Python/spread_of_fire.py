import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def spread_of_fire(grid_size, burn_probability, experiment_number):
    burned_percentages = []
    for i in range(experiment_number):
        grid = [['Tree' for i in range(grid_size)] for j in range(grid_size)]
        grid[grid_size // 2][grid_size // 2] = 'Burning'

        changed = True
        while changed:
            changed = False
            for i in range(grid_size):
                for j in range(grid_size):
                    if grid[i][j] == 'Burning':
                        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            new_i, new_j = i + di, j + dj
                            if 0 <= new_i < grid_size and 0 <= new_j < grid_size:
                                if grid[new_i][new_j] == 'Tree' and random.random() < burn_probability:
                                     grid[new_i][new_j] = 'Burning'
                                     changed = True

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

def ln_function(x, a, b):
    return a * np.log(x) + b

x = data["Burn Probability"]
y = data["Average Burned Percentage"]
popt, pcov = curve_fit(ln_function, x, y)
a, b = popt

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', label='Data')
plt.plot(x, ln_function(x, *popt), label='Fitted Curve')
plt.xlabel("Burn Probability")
plt.ylabel("Average Burned Percentage")
plt.title("Spread of Fire Simulation")
plt.legend()
plt.grid(True)
plt.show()

print("Curve fitting parameters:")
print("a =", a)
print("b =", b)