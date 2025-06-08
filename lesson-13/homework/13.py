import numpy as np
matx = np.random.rand(3, 3)
vec = np.random.rand(3, 1)
result = np.dot(matx, vec)
print("Matrix (3x3):\n", matx)
print("\nVector (3x1):\n", vec)
print("\nMatrix-Vector Product (3x1):\n", result)
