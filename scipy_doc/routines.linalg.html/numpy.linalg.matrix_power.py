import numpy as np
from numpy import linalg as la

i = np.array([[0, 1], [-1, 0]])  # matrix equiv. of the imaginary unit
la.matrix_power(i, 3)  # should = -i
la.matrix_power(np.matrix(i), 3)  # matrix arg returns matrix
la.matrix_power(i, 0)
la.matrix_power(i, -3)  # should = 1/(-i) = i, but w/ f.p. elements
q = np.zeros((4, 4))
q[0:2, 0:2] = -i
q[2:4, 2:4] = i
q  # one of the three quarternion units not equal to 1
la.matrix_power(q, 2)  # = -np.eye(4)
