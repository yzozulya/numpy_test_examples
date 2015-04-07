import numpy as np
from numpy import linalg as la

a = np.arange(9) - 4
a
b = a.reshape((3, 3))
b
la.norm(a)
la.norm(b)
la.norm(b, 'fro')
la.norm(a, np.inf)
la.norm(b, np.inf)
la.norm(a, -np.inf)
la.norm(b, -np.inf)
la.norm(a, 1)
la.norm(b, 1)
la.norm(a, -1)
la.norm(b, -1)
la.norm(a, 2)
la.norm(b, 2)
la.norm(a, -2)
la.norm(b, -2)
la.norm(a, 3)
la.norm(a, -3)
c = np.array([[1, 2, 3],
              [-1, 1, 4]])
la.norm(c, axis=0)
la.norm(c, axis=1)
la.norm(c, ord=1, axis=1)
m = np.arange(8).reshape(2, 2, 2)
la.norm(m, axis=(1, 2))
la.norm(m[0, :, :]), la.norm(m[1, :, :])
