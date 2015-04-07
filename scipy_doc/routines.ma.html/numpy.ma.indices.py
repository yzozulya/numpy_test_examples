import numpy as np

grid = np.indices((2, 3))
grid.shape
grid[0]  # row indices
grid[1]  # column indices
x = np.arange(20).reshape(5, 4)
row, col = np.indices((2, 3))
x[row, col]
