import numpy as np

for dt in [np.int32, np.int64, np.float64, np.complex128]:
    np.ma.array([0, 1], dtype=dt).get_fill_value()
x = np.ma.array([0, 1.], fill_value=-np.inf)
x.get_fill_value()
