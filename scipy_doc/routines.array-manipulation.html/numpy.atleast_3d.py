import numpy as np

np.atleast_3d(3.0)
x = np.arange(3.0)
np.atleast_3d(x).shape
x = np.arange(12.0).reshape(4, 3)
np.atleast_3d(x).shape
np.atleast_3d(x).base is x
for arr in np.atleast_3d([1, 2], [[1, 2]], [[[1, 2]]]):
    print
    arr, arr.shape
