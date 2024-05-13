import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *
import random

global EMPTY, TREE, BURNING
EMPTY = 0
TREE = 1
BURNING = 2

def initForest(n):
    forest = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            if (i == 8 and j == 8):
                forest[i, j] = BURNING
            else:
                forest[i, j] = TREE
    return forest

def spread(site, N, E, S, W, burnProbability):
    newSite = None
    if (site == EMPTY):
        newSite = EMPTY
    else:
        if (site == BURNING):
            newSite = EMPTY
        else:
            if (N == BURNING or E == BURNING or S == BURNING or W == BURNING):
                if (random.random() < burnProbability):
                    newSite = BURNING
                else:
                    newSite = TREE
    return newSite

def reflectingLat(lat):
    latNS = np.row_stack((lat[0], lat, lat[-1]))
    return np.column_stack((latNS[:,0], latNS, latNS[:,-1]))

def applyExtended(latExt, burnProbability):
    n = latExt.shape[0] - 2
    newLat = np.zeros((n, n))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            site = latExt[i, j]
            N = latExt[i + 1, j]
            E = latExt[i, j + 1]
            S = latExt[i - 1, j]
            W = latExt[i, j - 1]
            newLat[i - 1, j - 1] = spread(site, N, E, S, W, burnProbability)
    return newLat

def fire(n, burnProbability, t):
    forest  = initForest(n)

    grids = np.zeros((t + 1, n, n))
    grids[0, :, :] = forest
    for i in range(1, t + 1):
        forestExtended = reflectingLat(forest)
        forest = applyExtended(forestExtended, burnProbability)
        grids[i, :, :] = forest
    return grids

def treeBurned(grid, n):
    last_state = grid[-1].copy()
    burned = 0
    for i in range(n):
        for j in range(n):
            if last_state[i][j] == 2 or last_state[i][j] == 0:
                burned += 1
    percentage = burned/(n*n)
    return percentage

def logistic_function(x, a, b, c):
    return c / (1 + np.exp(-a * (x - b)))

def fit_logistic(burn_probs, burned_percentages):
    from scipy.optimize import curve_fit
    x_data = np.array(burn_probs)
    y_data = np.array(burned_percentages)
    popt_init = [1, 0.5, 0.5]
    popt, _ = curve_fit(logistic_function, x_data, y_data, p0=popt_init)

    return popt

n = 17
burn_probs = np.arange(.1, 1., .1)
num_sims = 10

burned_percentages = []
for burnProb in burn_probs:
    experiment = np.array([treeBurned(fire(n, burnProb, 20), n) for i in range(num_sims)])
    avg_burned = np.mean(experiment)
    burned_percentages.append(avg_burned)

fitted_params = fit_logistic(burn_probs, burned_percentages)

plt.plot(burn_probs, burned_percentages, 'o')
plt.plot(burn_probs, logistic_function(burn_probs, *fitted_params))
plt.xlabel("Burn Probability")
plt.ylabel("Average Burned Percentage")
plt.title("Spread of Fire")
plt.grid(True)
plt.show()