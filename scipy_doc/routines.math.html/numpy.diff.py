import numpy as np

x = np.array([1, 2, 4, 7, 0])
np.diff(x)
np.diff(x, n=2)
x = np.array([[1, 3, 6, 10], [0, 5, 6, 8]])
np.diff(x)
np.diff(x, axis=0)
