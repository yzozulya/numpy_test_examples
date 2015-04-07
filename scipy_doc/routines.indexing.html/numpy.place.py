import numpy as np

arr = np.arange(6).reshape(2, 3)
np.place(arr, arr > 2, [44, 55])
arr
