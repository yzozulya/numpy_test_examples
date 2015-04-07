import numpy as np

a = np.array([0, 1, 2])
np.tile(a, 2)
np.tile(a, (2, 2))
np.tile(a, (2, 1, 2))
b = np.array([[1, 2], [3, 4]])
np.tile(b, 2)
np.tile(b, (2, 1))
