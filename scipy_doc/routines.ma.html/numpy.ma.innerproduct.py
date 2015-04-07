import numpy as np

a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
np.inner(a, b)
a = np.arange(24).reshape((2, 3, 4))
b = np.arange(4)
np.inner(a, b)
np.inner(np.eye(2), 7)
