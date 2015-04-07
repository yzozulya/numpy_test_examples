import numpy as np

np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
