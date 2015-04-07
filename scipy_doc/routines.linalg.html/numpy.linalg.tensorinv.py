import numpy as np

a = np.eye(4 * 6)
a.shape = (4, 6, 8, 3)
ainv = np.linalg.tensorinv(a, ind=2)
ainv.shape
b = np.random.randn(4, 6)
np.allclose(np.tensordot(ainv, b), np.linalg.tensorsolve(a, b))
a = np.eye(4 * 6)
a.shape = (24, 8, 3)
ainv = np.linalg.tensorinv(a, ind=1)
ainv.shape
b = np.random.randn(24)
np.allclose(np.tensordot(ainv, b, 1), np.linalg.tensorsolve(a, b))
