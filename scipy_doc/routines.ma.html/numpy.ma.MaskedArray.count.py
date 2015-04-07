import numpy as np
import numpy.ma as ma

a = ma.arange(6).reshape((2, 3))
a[1, :] = ma.masked
a
a.count()
a.count(axis=0)
a.count(axis=1)
