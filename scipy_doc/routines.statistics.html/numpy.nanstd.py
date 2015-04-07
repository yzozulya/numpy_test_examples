import numpy as np

a = np.array([[1, np.nan], [3, 4]])
np.nanstd(a)
np.nanstd(a, axis=0)
np.nanstd(a, axis=1)
