import numpy as np

np.testing.assert_array_almost_equal([1.0, 2.333, np.nan],
                                     [1.0, 2.333, np.nan])

np.testing.assert_array_almost_equal([1.0, 2.33333, np.nan],
                                     [1.0, 2.33339, np.nan], decimal=5)

np.testing.assert_array_almost_equal([1.0, 2.33333, np.nan],
                                     [1.0, 2.33333, 5], decimal=5)