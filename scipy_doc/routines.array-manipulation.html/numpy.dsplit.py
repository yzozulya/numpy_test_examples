import numpy as np

x = np.arange(16.0).reshape(2, 2, 4)
x
np.dsplit(x, 2)
np.dsplit(x, np.array([3, 6]))
