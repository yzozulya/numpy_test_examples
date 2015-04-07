import numpy as np

x = np.array([[1, 2], [3, 4]])
np.repeat(x, 2)
np.repeat(x, 3, axis=1)
np.repeat(x, [1, 2], axis=0)
