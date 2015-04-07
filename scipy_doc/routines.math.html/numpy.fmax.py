import numpy as np

np.fmax([2, 3, 4], [1, 5, 2])
np.fmax(np.eye(2), [0.5, 2])
np.fmax([np.nan, 0, np.nan], [0, np.nan, np.nan])
