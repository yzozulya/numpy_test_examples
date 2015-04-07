import numpy as np

np.promote_types('f4', 'f8')
np.promote_types('i8', 'f4')
np.promote_types('>i8', '<c8')
np.promote_types('i4', 'S8')
