import numpy as np

x = np.arange(4).reshape((2, 2))
x
np.ptp(x, axis=0)
np.ptp(x, axis=1)
