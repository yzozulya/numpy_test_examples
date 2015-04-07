from numpy import *

linspace(0, 5, num=6)  # 6 evenly spaced numbers between 0 and 5 incl.
linspace(0, 5, num=10)  # 10 evenly spaced numbers between 0 and 5 incl.
linspace(0, 5, num=10, endpoint=False)  # 10 evenly spaced numbers between 0 and 5 EXCL.
stepsize = linspace(0, 5, num=10, endpoint=False, retstep=True)  # besides the usual array, also return the step size
stepsize
myarray, stepsize = linspace(0, 5, num=10, endpoint=False, retstep=True)
stepsize
