import numpy as np

np.unique1d([1, 1, 2, 2, 3, 3])
a = np.array([[1, 1], [2, 3]])
np.unique1d(a)
np.unique1d([1, 2, 6, 4, 2, 3, 2], return_index=True)
x = [1, 2, 6, 4, 2, 3, 2]
u, i = np.unique1d(x, return_inverse=True)
u
i
[u[p] for p in i]
