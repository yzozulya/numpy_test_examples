import numpy as np

np.find_common_type([], [np.int64, np.float32, np.complex])
np.find_common_type([np.int64, np.float32], [])
np.find_common_type([np.float32], [np.int64, np.float64])
np.find_common_type([np.float32], [np.complex])
np.find_common_type(['f4', 'f4', 'i4'], ['c8'])
