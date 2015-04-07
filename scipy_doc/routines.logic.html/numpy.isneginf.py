import numpy as np

np.isneginf(np.NINF)
np.isneginf(np.inf)
np.isneginf(np.PINF)
np.isneginf([-np.inf, 0., np.inf])
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
np.isneginf(x, y)
y
