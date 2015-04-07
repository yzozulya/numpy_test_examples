import numpy as np
import numpy.ma as ma

x = np.array([1, 1.1, 2, 1.1, 3])
ma.masked_values(x, 1.1)
ma.masked_values(x, 1.5)
x = np.arange(5)
x
ma.masked_values(x, 2)
ma.masked_equal(x, 2)
