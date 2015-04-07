import numpy as np

a = np.array([[1, 2], [3, np.nan]])
np.nanmin(a)
np.nanmin(a, axis=0)
np.nanmin(a, axis=1)
np.nanmin([1, 2, np.nan, np.inf])
np.nanmin([1, 2, np.nan, np.NINF])
