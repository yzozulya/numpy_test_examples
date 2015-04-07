import numpy as np

np.array(a, copy=True)
x = np.array([1, 2, 3])
y = x
z = np.copy(x)
x[0] = 10
x[0] == y[0]
x[0] == z[0]
