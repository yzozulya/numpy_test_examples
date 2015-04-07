import numpy as np

np.trace(np.eye(3))
a = np.arange(8).reshape((2, 2, 2))
np.trace(a)
a = np.arange(24).reshape((2, 2, 2, 3))
np.trace(a).shape
