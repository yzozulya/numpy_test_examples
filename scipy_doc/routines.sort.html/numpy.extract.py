import numpy as np

arr = np.arange(12).reshape((3, 4))
arr
condition = np.mod(arr, 3) == 0
condition
np.extract(condition, arr)
arr[condition]
