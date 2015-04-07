import numpy as np

np.atleast_2d(3.0)
x = np.arange(3.0)
np.atleast_2d(x)
np.atleast_2d(x).base is x
np.atleast_2d(1, [1, 2], [[1, 2]])
