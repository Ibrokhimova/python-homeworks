import numpy as np
matx=np.random.rand(5,5)
min_val = matx.min()
max_val = matx.max()
normalized_matrix = (matx-min_val)/(matx-min_val)
print("Original matrix:", matx)
print("Normalized matrix:", normalized_matrix)