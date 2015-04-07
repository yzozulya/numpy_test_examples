import numpy as np

np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
np.append([[1, 2, 3], [4, 5, 6]], [7, 8, 9], axis=0)
