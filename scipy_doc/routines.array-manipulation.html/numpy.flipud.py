import numpy as np

A = np.diag([1.0, 2, 3])
A
np.flipud(A)
A = np.random.randn(2, 3, 5)
np.all(np.flipud(A) == A[::-1, ...])
np.flipud([1, 2])
