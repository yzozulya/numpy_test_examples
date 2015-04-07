from __future__ import with_statement  # use 'with' in Python 2.5
import numpy as np

olderr = np.seterr(all='ignore')  # Set error handling to known state.
np.arange(3) / 0.
with np.errstate(divide='warn'):
    np.arange(3) / 0.
np.sqrt(-1)
with np.errstate(invalid='raise'):
    np.sqrt(-1)
np.geterr()
