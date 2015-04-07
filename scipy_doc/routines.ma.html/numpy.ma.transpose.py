import numpy as np
import numpy.ma as ma

x = ma.arange(4).reshape((2, 2))
x[1, 1] = ma.masked
ma.transpose(x)
