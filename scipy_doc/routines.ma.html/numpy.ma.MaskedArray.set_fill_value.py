import numpy as np

x = np.ma.array([0, 1.], fill_value=-np.inf)
x.fill_value
x.set_fill_value(np.pi)
x.fill_value
x.set_fill_value()
x.fill_value
