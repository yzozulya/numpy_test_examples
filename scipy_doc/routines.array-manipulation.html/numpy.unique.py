import numpy as np

np.unique([1, 1, 2, 2, 3, 3])
a = np.array([[1, 1], [2, 3]])
np.unique(a)
a = np.array(['a', 'b', 'b', 'c', 'a'])
u, indices = np.unique(a, return_index=True)
u
indices
a[indices]
a = np.array([1, 2, 6, 4, 2, 3, 2])
u, indices = np.unique(a, return_inverse=True)
u
indices
u[indices]
