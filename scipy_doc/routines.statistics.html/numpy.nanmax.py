import numpy as np

a = np.array([[1, 2], [3, np.nan]])
np.nanmax(a)
np.nanmax(a, axis=0)
np.nanmax(a, axis=1)
np.nanmax([1, 2, np.nan, np.NINF])
np.nanmax([1, 2, np.nan, np.inf])
