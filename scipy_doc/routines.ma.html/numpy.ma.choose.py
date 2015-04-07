import numpy as np

choice = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
a = np.array([2, 1, 0])
np.ma.choose(a, choice)
