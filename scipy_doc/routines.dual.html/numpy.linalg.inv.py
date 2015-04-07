import numpy as np
from numpy.linalg import inv

a = np.array([[1., 2.], [3., 4.]])
ainv = inv(a)
np.allclose(np.dot(a, ainv), np.eye(2))
np.allclose(np.dot(ainv, a), np.eye(2))
ainv = inv(np.matrix(a))
ainv
a = np.array([[[1., 2.], [3., 4.]], [[1, 3], [3, 5]]])
inv(a)
