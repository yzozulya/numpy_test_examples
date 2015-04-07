import numpy as np

dfnum = 1.  # between group degrees of freedom
dfden = 48.  # within groups degrees of freedom
s = np.random.f(dfnum, dfden, 1000)
sort(s)[-10]
