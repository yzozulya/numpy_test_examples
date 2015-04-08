import numpy as np
import numpy.linalg as la

A = np.array([[1, -2j], [2j, 5]])
A
L = np.linalg.cholesky(A)
L
np.dot(L, L.T.conj())  # verify that L * L.H = A
A = [[1, -2j], [2j, 5]]  # what happens if A is only array_like?
np.linalg.cholesky(A)  # an ndarray object is returned
# But a matrix object is returned if A is a matrix object
la.cholesky(np.matrix(A))
