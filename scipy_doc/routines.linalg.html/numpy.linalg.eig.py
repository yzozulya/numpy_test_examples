import numpy as np
from numpy import linalg as la

w, v = la.eig(np.diag((1, 2, 3)))
w
v
w, v = la.eig(np.array([[1, -1], [1, 1]]))
w
v
a = np.array([[1, 1j], [-1j, 1]])
w, v = la.eig(a)
w
v
a = np.array([[1 + 1e-9, 0], [0, 1 - 1e-9]])
# Theor. e-values are 1 +/- 1e-9
w, v = la.eig(a)
w
v
