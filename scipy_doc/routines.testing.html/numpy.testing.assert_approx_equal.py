import numpy as np

np.testing.assert_approx_equal(0.12345677777777e-20, 0.1234567e-20)
np.testing.assert_approx_equal(0.12345670e-20, 0.12345671e-20,
                               significant=8)
np.testing.assert_approx_equal(0.12345670e-20, 0.12345672e-20,
                               significant=8)
abs(0.12345670e-20 / 1e-21 - 0.12345672e-20 / 1e-21) >= 10 ** -(8 - 1)