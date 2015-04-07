import numpy as np
from numpy.ma import flatnotmasked_edges

a = np.ma.arange(10)
flatnotmasked_edges(a)
mask = (a < 3) | (a > 8) | (a == 5)
a[mask] = np.ma.masked
np.array(a[~a.mask])
flatnotmasked_edges(a)
a[:] = np.ma.masked
print
flatnotmasked_edges(np.ma)
