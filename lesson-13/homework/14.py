import numpy as np
A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A, b)
print("Matrix A:\n", A)
print("\nVector b:\n", b)
print("\nSolution x:\n", x)
