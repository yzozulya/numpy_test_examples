import numpy as np

np.nansum(1)
np.nansum([1])
np.nansum([1, np.nan])
a = np.array([[1, 1], [1, np.nan]])
np.nansum(a)
np.nansum(a, axis=0)
np.nansum([1, np.nan, np.inf])
np.nansum([1, np.nan, np.NINF])
np.nansum([1, np.nan, np.inf, -np.inf])  # both +/- infinity present
