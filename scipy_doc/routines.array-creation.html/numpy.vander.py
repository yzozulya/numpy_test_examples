import numpy as np

x = np.array([1, 2, 3, 5])
N = 3
np.vander(x, N)
np.column_stack([x ** (N - 1 - i) for i in range(N)])
x = np.array([1, 2, 3, 5])
np.vander(x)
np.vander(x, increasing=True)
np.linalg.det(np.vander(x))
(5 - 3) * (5 - 2) * (5 - 1) * (3 - 2) * (3 - 1) * (2 - 1)
