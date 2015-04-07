import numpy as np
import numpy.ma as ma

a = np.arange(5, dtype=np.float)
a[2] = np.NaN
a[3] = np.PINF
a
ma.masked_invalid(a)
