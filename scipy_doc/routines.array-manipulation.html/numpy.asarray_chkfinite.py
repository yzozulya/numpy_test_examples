import numpy as np

a = [1, 2]
np.asarray_chkfinite(a, dtype=float)
a = [1, 2, np.inf]
try:
    np.asarray_chkfinite(a)
except ValueError:
    print
    'ValueError'
