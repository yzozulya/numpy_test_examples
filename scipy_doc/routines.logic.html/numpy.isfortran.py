import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]], order='C')
a
np.isfortran(a)
b = np.array([[1, 2, 3], [4, 5, 6]], order='FORTRAN')
b
np.isfortran(b)
a = np.array([[1, 2, 3], [4, 5, 6]], order='C')
a
np.isfortran(a)
b = a.T
b
np.isfortran(b)
np.isfortran(np.array([1, 2], order='FORTRAN'))
