import numpy as np
matrix = np.random.rand(5, 5)
row_sums = np.sum(matrix, axis=1)
col_sums = np.sum(matrix, axis=0)
print("Matrix:\n", matrix)
print("\nRow-wise sums:", row_sums)
print("Column-wise sums:", col_sums)
