import numpy as np

np.isposinf(np.PINF)
np.isposinf(np.inf)
np.isposinf(np.NINF)
np.isposinf([-np.inf, 0., np.inf])
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
np.isposinf(x, y)
y
