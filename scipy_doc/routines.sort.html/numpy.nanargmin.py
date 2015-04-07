import numpy as np

a = np.array([[np.nan, 4], [2, 3]])
np.argmin(a)
np.nanargmin(a)
np.nanargmin(a, axis=0)
np.nanargmin(a, axis=1)
