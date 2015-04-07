from numpy import *

myslice = index_exp[2:4, ..., 4, ::-1]  # myslice could now be passed to a function, for example.
print myslice
