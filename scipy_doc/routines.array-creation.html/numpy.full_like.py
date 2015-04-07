import numpy as np

x = np.arange(6, dtype=np.int)
np.full_like(x, 1)
np.full_like(x, 0.1)
np.full_like(x, 0.1, dtype=np.double)
np.full_like(x, np.nan, dtype=np.double)
y = np.arange(6, dtype=np.double)
np.full_like(y, 0.1)
