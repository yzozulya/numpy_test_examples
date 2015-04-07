import numpy as np

np.minimum([2, 3, 4], [1, 5, 2])
np.minimum(np.eye(2), [0.5, 2])  # broadcasting
np.minimum([np.nan, 0, np.nan], [0, np.nan, np.nan])
np.minimum(-np.Inf, 1)
