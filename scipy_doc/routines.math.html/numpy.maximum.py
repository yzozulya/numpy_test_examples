import numpy as np

np.maximum([2, 3, 4], [1, 5, 2])
np.maximum(np.eye(2), [0.5, 2])  # broadcasting
np.maximum([np.nan, 0, np.nan], [0, np.nan, np.nan])
np.maximum(np.Inf, 1)
