import numpy as np

a = np.array([1, 2, 3])
np.cumprod(a)  # intermediate results 1, 1*2
# total product 1*2*3 = 6
a = np.array([[1, 2, 3], [4, 5, 6]])
np.cumprod(a, dtype=float)  # specify type of output
np.cumprod(a, axis=0)
np.cumprod(a, axis=1)
