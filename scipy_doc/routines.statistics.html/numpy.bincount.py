import numpy as np

np.bincount(np.arange(5))
np.bincount(np.array([0, 1, 1, 3, 2, 1, 7]))
x = np.array([0, 1, 1, 3, 2, 1, 7, 23])
np.bincount(x).size == np.amax(x) + 1
np.bincount(np.arange(5, dtype=np.float))
w = np.array([0.3, 0.5, 0.2, 0.7, 1., -0.6])  # weights
x = np.array([0, 1, 1, 2, 2, 2])
np.bincount(x, weights=w)
