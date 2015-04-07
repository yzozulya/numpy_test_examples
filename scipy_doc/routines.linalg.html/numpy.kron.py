import numpy as np

np.kron([1, 10, 100], [5, 6, 7])
np.kron([5, 6, 7], [1, 10, 100])
np.kron(np.eye(2), np.ones((2, 2)))
a = np.arange(100).reshape((2, 5, 2, 5))
b = np.arange(24).reshape((2, 3, 4))
c = np.kron(a, b)
c.shape
I = (1, 3, 0, 2)
J = (0, 2, 1)
J1 = (0,) + J  # extend to ndim=4
S1 = (1,) + b.shape
K = tuple(np.array(I) * np.array(S1) + np.array(J1))
c[K] == a[I] * b[J]
