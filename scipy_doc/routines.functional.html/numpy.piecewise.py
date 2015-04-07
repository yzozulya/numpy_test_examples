import numpy as np

x = np.linspace(-2.5, 2.5, 6)
np.piecewise(x, [x < 0, x >= 0], [-1, 1])
np.piecewise(x, [x < 0, x >= 0], [lambda x_: -x_, lambda x_: x_])
