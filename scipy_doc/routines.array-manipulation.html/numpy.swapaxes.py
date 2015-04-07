import numpy as np

x = np.array([[1, 2, 3]])
np.swapaxes(x, 0, 1)
x = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
x
np.swapaxes(x, 0, 2)
