import numpy as np

x = np.ma.array([0, 1.], fill_value=3)
y = np.ma.array([0, 1.], fill_value=3)
np.ma.common_fill_value(x, y)
