import numpy as np

iterable = (x * x for x in range(5))
np.fromiter(iterable, np.float)
