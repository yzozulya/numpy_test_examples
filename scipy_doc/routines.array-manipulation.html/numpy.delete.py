import numpy as np

arr = np.array([1, 2, 3, 4])
mask = np.ones(len(arr), dtype=bool)
mask[[0, 2, 4]] = False
result = arr[mask, ...]
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
arr
np.delete(arr, 1, 0)
np.delete(arr, np.s_[::2], 1)
np.delete(arr, [1, 3, 5], None)
