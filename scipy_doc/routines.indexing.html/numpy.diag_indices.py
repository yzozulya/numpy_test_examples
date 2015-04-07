import numpy as np

di = np.diag_indices(4)
di
a = np.arange(16).reshape(4, 4)
a
a[di] = 100
a
d3 = np.diag_indices(2, 3)
d3
a = np.zeros((2, 2, 2), dtype=np.int)
a[d3] = 1
a
