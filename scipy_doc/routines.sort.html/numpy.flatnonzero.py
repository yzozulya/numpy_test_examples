import numpy as np

x = np.arange(-2, 3)
x
np.flatnonzero(x)
x.ravel()[np.flatnonzero(x)]
