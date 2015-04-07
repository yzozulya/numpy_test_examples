import numpy as np

x = np.array([3, 4, 2, 1])
x[np.argpartition(x, 3)]
x[np.argpartition(x, (1, 3))]
