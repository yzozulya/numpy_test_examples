import numpy as np
from numpy import linalg as la

a = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
a
la.cond(a)
la.cond(a, 'fro')
la.cond(a, np.inf)
la.cond(a, -np.inf)
la.cond(a, 1)
la.cond(a, -1)
la.cond(a, 2)
la.cond(a, -2)
min(la.svd(a, compute_uv=0)) * min(la.svd(la.inv(a), compute_uv=0))
