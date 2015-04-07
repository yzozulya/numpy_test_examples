import numpy as np
import numpy.testing as npt

npt.assert_almost_equal(2.3333333333333, 2.33333334)
npt.assert_almost_equal(2.3333333333333, 2.33333334, decimal=10)
npt.assert_almost_equal(np.array([1.0, 2.3333333333333]),
                        np.array([1.0, 2.33333334]), decimal=9)
