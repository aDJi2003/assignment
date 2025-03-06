import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-5, -8]

A = [[6, 5], [9, 4], [1, 2]]
b = [30, 36, 10]

x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

print("Optimal solution:")
print(f"X1 = {res.x[0]:.2f}, X2 = {res.x[1]:.2f}")
print(f"Optimal value = {-res.fun:.2f}")

x = np.linspace(0, 10, 400)
y1 = (30 - 6*x) / 5
y2 = (36 - 9*x) / 4
y3 = (10 - x) / 2

y1 = np.maximum(y1, 0)
y2 = np.maximum(y2, 0)
y3 = np.maximum(y3, 0)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='6X1 + 5X2 ≤ 30')
plt.plot(x, y2, label='9X1 + 4X2 ≤ 36')
plt.plot(x, y3, label='X1 + 2X2 ≤ 10')
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, where=(x >= 0), color='gray', alpha=0.3)

plt.scatter(res.x[0], res.x[1], color='red', marker='o', label='Optimal Solution')
plt.xlabel('X1')
plt.ylabel('X2')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend()
plt.title('Feasible Region and Optimal Solution')
plt.grid()
plt.show()