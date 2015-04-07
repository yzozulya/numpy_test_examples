import numpy as np

np.atleast_1d(1.0)
x = np.arange(9.0).reshape(3, 3)
np.atleast_1d(x)
np.atleast_1d(x) is x
np.atleast_1d(1, [3, 4])
