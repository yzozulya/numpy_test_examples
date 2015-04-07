import numpy as np
import numpy.ma as ma

x = ma.array([1, 2, 4])
x[1] = ma.masked
x
np.expand_dims(x, axis=0)
ma.expand_dims(x, axis=0)
x[np.newaxis, :]
