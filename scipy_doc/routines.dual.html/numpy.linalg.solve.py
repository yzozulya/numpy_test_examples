import numpy as np

a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)
x
np.allclose(np.dot(a, x), b)
