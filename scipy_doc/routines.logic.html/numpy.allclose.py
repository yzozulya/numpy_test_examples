import numpy as np

np.allclose([1e10, 1e-7], [1.00001e10, 1e-8])
np.allclose([1e10, 1e-8], [1.00001e10, 1e-9])
np.allclose([1e10, 1e-8], [1.0001e10, 1e-9])
np.allclose([1.0, np.nan], [1.0, np.nan])
