import numpy as np

a = np.ma.MaskedArray()
a_min = 1
a_max = 10

a.clip(a_min, a_max, out=None)