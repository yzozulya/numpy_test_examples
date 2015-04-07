import numpy as np

np.fromstring('\x01\x02', dtype=np.uint8)
np.fromstring('1 2', dtype=int, sep=' ')
np.fromstring('1, 2', dtype=int, sep=',')
np.fromstring('\x01\x02\x03\x04\x05', dtype=np.uint8, count=3)
