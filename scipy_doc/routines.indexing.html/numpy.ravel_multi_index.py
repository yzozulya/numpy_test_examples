import numpy as np

arr = np.array([[3, 6, 6], [4, 5, 1]])
np.ravel_multi_index(arr, (7, 6))
np.ravel_multi_index(arr, (7, 6), order='F')
np.ravel_multi_index(arr, (4, 6), mode='clip')
np.ravel_multi_index(arr, (4, 4), mode=('clip', 'wrap'))
np.ravel_multi_index((3, 1, 4, 1), (6, 7, 8, 9))
