import numpy as np

a = np.arange(4).reshape((2, 2))
a
np.amin(a)  # Minimum of the flattened array
np.amin(a, axis=0)  # Minima along the first axis
np.amin(a, axis=1)  # Minima along the second axis
b = np.arange(5, dtype=np.float)
b[2] = np.NaN
np.amin(b)
np.nanmin(b)
