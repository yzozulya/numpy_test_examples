import numpy as np

a = np.zeros((10, 2))
b = a.T
c = b.view()
c.shape = 20
a = np.arange(6).reshape((3, 2))
a
np.reshape(a, (2, 3))  # C-like index ordering
np.reshape(np.ravel(a), (2, 3))  # equivalent to C ravel then C reshape
np.reshape(a, (2, 3), order='F')  # Fortran-like index ordering
np.reshape(np.ravel(a, order='F'), (2, 3), order='F')
a = np.array([[1, 2, 3], [4, 5, 6]])
np.reshape(a, 6)
np.reshape(a, 6, order='F')
np.reshape(a, (3, -1))  # the unspecified value is inferred to be 2
