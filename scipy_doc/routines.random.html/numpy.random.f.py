import numpy as np
from numpy.ma import sort

dfnum = 1.  # between group degrees of freedom
dfden = 48.  # within groups degrees of freedom
s = np.random.f(dfnum, dfden, 1000)
sort(s)[-10]
