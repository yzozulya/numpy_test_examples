import numpy as np

a = np.array([[1, np.nan], [3, 4]])
np.var(a)
np.nanvar(a, axis=0)
np.nanvar(a, axis=1)
