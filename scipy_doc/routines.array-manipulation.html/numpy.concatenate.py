import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0)
np.concatenate((a, b.T), axis=1)
a = np.ma.arange(3)
a[1] = np.ma.masked
b = np.arange(2, 5)
a
b
np.concatenate([a, b])
np.ma.concatenate([a, b])
