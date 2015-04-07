import numpy as np

x = np.array([536870910, 536870910, 536870910, 536870910])
np.prod(x)  # random
np.prod([1., 2.])
np.prod([[1., 2.], [3., 4.]])
np.prod([[1., 2.], [3., 4.]], axis=1)
x = np.array([1, 2, 3], dtype=np.uint8)
np.prod(x).dtype == np.uint
x = np.array([1, 2, 3], dtype=np.int8)
np.prod(x).dtype == np.int
