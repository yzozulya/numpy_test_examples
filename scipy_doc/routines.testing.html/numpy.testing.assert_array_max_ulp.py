import numpy as np

a = np.linspace(0., 1., 100)
res = np.testing.assert_array_max_ulp(a, np.arcsin(np.sin(a)))
