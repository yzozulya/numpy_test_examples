import numpy as np

np.copysign(1.3, -1)
1 / np.copysign(0, 1)
1 / np.copysign(0, -1)
np.copysign([-1, 0, 1], -1.1)
np.copysign([-1, 0, 1], np.arange(3) - 1)
