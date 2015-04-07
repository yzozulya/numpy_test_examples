import numpy as np

a = [1, 2]
np.asarray(a)
a = np.array([1, 2])
np.asarray(a) is a
a = np.array([1, 2], dtype=np.float32)
np.asarray(a, dtype=np.float32) is a
np.asarray(a, dtype=np.float64) is a
issubclass(np.matrix, np.ndarray)
a = np.matrix([[1, 2]])
np.asarray(a) is a
np.asanyarray(a) is a
