import numpy as np
A = np.random.rand(3, 4)
B = np.random.rand(4, 3)
C = np.dot(A, B)
print("Matrix A:", A)
print("\n Matrix B:",B)
print("\nProduct (A · B) (3x3):\n", C)