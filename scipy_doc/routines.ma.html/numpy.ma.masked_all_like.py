import numpy as np
import numpy.ma as ma

arr = np.zeros((2, 3), dtype=np.float32)
arr
ma.masked_all_like(arr)
arr.dtype
ma.masked_all_like(arr).dtype
