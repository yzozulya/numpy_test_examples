import numpy as np

a = np.eye(2 * 3 * 4)
a.shape = (2 * 3, 4, 2, 3, 4)
b = np.random.randn(2 * 3, 4)
x = np.linalg.tensorsolve(a, b)
x.shape
np.allclose(np.tensordot(a, x, axes=3), b)
