from numpy import *

array([1.2345, -1.647]).round()  # rounds the items. Type remains float64.
array([1, -1]).round()  # integer arrays stay as they are
array([1.2345, -1.647]).round(decimals=1)  # round to 1 decimal place
array([1.2345 + 2.34j, -1.647 - 0.238j]).round()  # both real and complex parts are rounded
array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5]).round()  # numpy rounds x.5 to nearest even.
a = zeros(3, dtype=int)
array([1.2345, -1.647, 3.141]).round(out=a)  # different output arrays may be specified
a  # and the output is cast to the new type
round_(array([1.2345, -1.647]))  # round_ is the functional form. -> a copy.
around(array([1.2345, -1.647]))  # around is an alias of round_.
