import numpy as np
import numpy.matlib

a0 = np.array(1)
np.matlib.repmat(a0, 2, 3)
a1 = np.arange(4)
np.matlib.repmat(a1, 2, 2)
a2 = np.asmatrix(np.arange(6).reshape(2, 3))
np.matlib.repmat(a2, 2, 3)
