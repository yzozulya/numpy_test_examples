import numpy as np

np.testing.assert_array_equal([1.0, 2.33333, np.nan],
                              [np.exp(0), 2.33333, np.nan])
np.testing.assert_array_equal([1.0, np.pi, np.nan],
                              [1, np.sqrt(np.pi) ** 2, np.nan])
np.testing.assert_allclose([1.0, np.pi, np.nan],
                           [1, np.sqrt(np.pi) ** 2, np.nan],
                           rtol=1e-10, atol=0)
