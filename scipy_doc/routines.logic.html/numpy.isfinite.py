import numpy as np

np.isfinite(1)
np.isfinite(0)
np.isfinite(np.nan)
np.isfinite(np.inf)
np.isfinite(np.NINF)
np.isfinite([np.log(-1.), 1., np.log(0)])
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
np.isfinite(x, y)
y
