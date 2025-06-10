import numpy as np
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
B = np.array([12, -5, 15])
current = np.linalg.solve(A, B)
print("Currents [I1, I2, I3]:", current)
