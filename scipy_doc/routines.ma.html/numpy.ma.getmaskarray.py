import numpy as np
import numpy.ma as ma

a = ma.masked_equal([[1, 2], [3, 4]], 2)
a
ma.getmaskarray(a)
b = ma.masked_array([[1, 2], [3, 4]])
b
ma.getmaskarray(b)
