import numpy as np

a = np.ma.arange(10)
np.ma.extras.flatnotmasked_contiguous(a)
mask = (a < 3) | (a > 8) | (a == 5)
a[mask] = np.ma.masked
np.array(a[~a.mask])
np.ma.extras.flatnotmasked_contiguous(a)
a[:] = np.ma.masked
print
np.ma.extras.flatnotmasked_edges(a)
