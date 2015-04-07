import numpy as np

np.array_equiv([1, 2], [1, 2])
np.array_equiv([1, 2], [1, 3])
np.array_equiv([1, 2], [[1, 2], [1, 2]])
np.array_equiv([1, 2], [[1, 2, 1, 2], [1, 2, 1, 2]])
np.array_equiv([1, 2], [[1, 2], [1, 3]])
