import numpy as np

x = np.arange(4).reshape((2, 2))
x
np.transpose(x)
x = np.ones((1, 2, 3))
np.transpose(x, (1, 0, 2)).shape
