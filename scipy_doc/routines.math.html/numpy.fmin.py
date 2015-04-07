import numpy as np

np.fmin([2, 3, 4], [1, 5, 2])
np.fmin(np.eye(2), [0.5, 2])
np.fmin([np.nan, 0, np.nan], [0, np.nan, np.nan])
