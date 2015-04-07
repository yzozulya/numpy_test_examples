import numpy as np
from numpy import linalg as la

a = np.array([[1, -2j], [2j, 5]])
a
w, v = la.eigh(a)
w
v
np.dot(a, v[:, 0]) - w[0] * v[:, 0]  # verify 1st e-val/vec pair
np.dot(a, v[:, 1]) - w[1] * v[:, 1]  # verify 2nd e-val/vec pair
A = np.matrix(a)  # what happens if input is a matrix object
A
w, v = la.eigh(A)
w
v
