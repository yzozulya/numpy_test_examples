import numpy as np
import numpy.ma as ma

a = np.arange(9).reshape((3, 3))
a = ma.array(a)
a[1, 0] = ma.masked
a[1, 2] = ma.masked
a[2, 1] = ma.masked
a
ma.count_masked(a)
ma.count_masked(a, axis=0)
ma.count_masked(a, axis=1)
