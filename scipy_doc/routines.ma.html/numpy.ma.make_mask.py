import numpy as np
import numpy.ma as ma

m = [True, False, True, True]
ma.make_mask(m)
m = [1, 0, 1, 1]
ma.make_mask(m)
m = [1, 0, 2, -3]
ma.make_mask(m)
m = np.zeros(4)
m
ma.make_mask(m)
ma.make_mask(m, shrink=False)
m = [1, 0, 1, 1]
n = [0, 1, 0, 0]
arr = []
for man, mouse in zip(m, n):
    arr.append((man, mouse))
arr
dtype = np.dtype({'names': ['man', 'mouse'], })
arr = np.array(arr, dtype=dtype)
arr
ma.make_mask(arr, dtype=dtype)
