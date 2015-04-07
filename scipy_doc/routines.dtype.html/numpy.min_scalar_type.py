import numpy as np

np.min_scalar_type(10)
np.min_scalar_type(-260)
np.min_scalar_type(3.1)
np.min_scalar_type(1e50)
print(np.min_scalar_type(np.arange(4, dtype='f8')))
