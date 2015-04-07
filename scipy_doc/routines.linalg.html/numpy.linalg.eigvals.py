import numpy as np
from numpy import linalg as la

x = np.random.random()
Q = np.array([[np.cos(x), -np.sin(x)], [np.sin(x), np.cos(x)]])
la.norm(Q[0, :]), la.norm(Q[1, :]), np.dot(Q[0, :], Q[1, :])
D = np.diag((-1, 1))
la.eigvals(D)
A = np.dot(Q, D)
A = np.dot(A, Q.T)
la.eigvals(A)
