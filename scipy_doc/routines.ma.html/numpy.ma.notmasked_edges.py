import numpy as np

a = np.arange(9).reshape((3, 3))
m = np.zeros_like(a)
m[1:, 1:] = 1
am = np.ma.array(a, mask=m)
np.array(am[~am.mask])
np.ma.extras.notmasked_edges(ma)
