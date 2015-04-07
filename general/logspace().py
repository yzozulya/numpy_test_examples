from numpy import *

logspace(-2, 3, num=6)  # 6 evenly spaced pts on a logarithmic scale, from 10^{-2} to 10^3 incl.
logspace(-2, 3, num=10)  # 10 evenly spaced pts on a logarithmic scale, from 10^{-2} to 10^3 incl.
logspace(-2, 3, num=6, endpoint=False)  # 6 evenly spaced pts on a logarithmic scale, from 10^{-2} to 10^3 EXCL.
exp(linspace(log(0.01), log(1000), num=6, endpoint=False))  # for comparison
