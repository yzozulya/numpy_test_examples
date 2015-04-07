import numpy as np

a = np.array([1 + 2j, 3 + 4j, 5 + 6j])
a.imag
a.imag = np.array([8, 10, 12])
a
