import numpy as np
import numpy.ma as ma

x = [0.31, 1.2, 0.01, 0.2, -0.4, -1.1]
ma.masked_outside(x, -0.3, 0.3)
ma.masked_outside(x, 0.3, -0.3)
