import numpy as np
import numpy.ma as ma

a = np.zeros((3, 3), dtype=np.int)
a[1, 1] = 1
a
a = ma.masked_equal(a, 1)
a
ma.mask_cols(a)
