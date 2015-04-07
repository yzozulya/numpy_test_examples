import numpy as np

x = np.array([1., 1e-10, 1e-20])
eps = np.finfo(x.dtype).eps
np.testing.assert_array_almost_equal_nulp(x, x * eps / 2 + x)
np.testing.assert_array_almost_equal_nulp(x, x * eps + x)
