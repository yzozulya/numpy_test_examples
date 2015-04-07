import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
a
np.cumsum(a)
np.cumsum(a, dtype=float)  # specifies type of output value(s)
np.cumsum(a, axis=0)  # sum over rows for each of the 3 columns
np.cumsum(a, axis=1)  # sum over columns for each of the 2 rows
