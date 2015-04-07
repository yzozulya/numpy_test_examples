import numpy as np

a = np.arange(4).reshape((2, 2))
a
np.amax(a)  # Maximum of the flattened array
np.amax(a, axis=0)  # Maxima along the first axis
np.amax(a, axis=1)  # Maxima along the second axis
b = np.arange(5, dtype=np.float)
b[2] = np.NaN
np.amax(b)
np.nanmax(b)
