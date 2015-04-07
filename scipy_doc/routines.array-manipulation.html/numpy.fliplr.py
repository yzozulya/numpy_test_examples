import numpy as np

A = np.diag([1., 2., 3.])
A
np.fliplr(A)
A = np.random.randn(2, 3, 5)
np.all(np.fliplr(A) == A[:, ::-1, ...])
