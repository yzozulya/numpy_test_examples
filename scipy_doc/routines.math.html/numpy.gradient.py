import numpy as np

x = np.array([1, 2, 4, 7, 11, 16], dtype=np.float)
np.gradient(x)
np.gradient(x, 2)
np.gradient(np.array([[1, 2, 6], [3, 4, 5]], dtype=np.float))
x = np.array([0, 1, 2, 3, 4])
dx = np.gradient(x)
y = x ** 2
np.gradient(y, dx, edge_order=2)
