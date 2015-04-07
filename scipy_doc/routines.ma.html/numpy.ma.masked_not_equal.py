import numpy as np
import numpy.ma as ma

a = np.arange(4)
a
ma.masked_not_equal(a, 2)
