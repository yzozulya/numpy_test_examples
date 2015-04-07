import numpy as np
import numpy.ma as ma

a = ma.array([[1, 2], [3, 4]])
a[0, 1] = ma.masked
a
np.resize(a, (3, 3))
ma.resize(a, (3, 3))
a = np.array([[1, 2], [3, 4]])
ma.resize(a, (3, 3))
