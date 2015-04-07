import numpy as np

np.isinf(np.inf)
np.isinf(np.nan)
np.isinf(np.NINF)
np.isinf([np.inf, -np.inf, 1.0, np.nan])
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
np.isinf(x, y)
y
