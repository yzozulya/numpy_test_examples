import numpy as np
import numpy.ma as ma

a = np.arange(5)
a
a = ma.masked_where(a < 3, a)
a
ma.set_fill_value(a, -999)
a
a = range(5)
a
ma.set_fill_value(a, 100)
a
a = np.arange(5)
a
ma.set_fill_value(a, 100)
a
