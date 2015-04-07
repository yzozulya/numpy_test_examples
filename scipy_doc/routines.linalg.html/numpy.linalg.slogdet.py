import numpy as np

a = np.array([[1, 2], [3, 4]])
(sign, logdet) = np.linalg.slogdet(a)
(sign, logdet)
sign * np.exp(logdet)
a = np.array([[[1, 2], [3, 4]], [[1, 2], [2, 1]], [[1, 3], [3, 1]]])
a.shape
sign, logdet = np.linalg.slogdet(a)
(sign, logdet)
sign * np.exp(logdet)
np.linalg.det(np.eye(500) * 0.1)
np.linalg.slogdet(np.eye(500) * 0.1)
