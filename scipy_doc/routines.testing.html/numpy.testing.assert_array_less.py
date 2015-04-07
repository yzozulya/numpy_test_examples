import numpy as np

np.testing.assert_array_less([1.0, 1.0, np.nan], [1.1, 2.0, np.nan])
np.testing.assert_array_less([1.0, 1.0, np.nan], [1, 2.0, np.nan])
np.testing.assert_array_less([1.0, 4.0], 3)
np.testing.assert_array_less([1.0, 2.0, 3.0], [4])
