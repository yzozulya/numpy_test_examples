import numpy as np
import numpy.ma as ma

a = np.arange(4)
a
ma.masked_less_equal(a, 2)
