import numpy as np

x = np.array([-1, +1, +1, -1])
y = np.array([-1, -1, +1, +1])
np.arctan2(y, x) * 180 / np.pi
np.arctan2([1., -1.], [0., 0.])
np.arctan2([0., 0., np.inf], [+0., -0., np.inf])
