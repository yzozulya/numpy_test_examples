import numpy as np

a = np.array([[1, np.nan], [3, 4]])
np.nanmean(a)
np.nanmean(a, axis=0)
np.nanmean(a, axis=1)
