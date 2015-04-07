from numpy import *

a = 25
binary_repr(a)  # binary representation of 25
b = float_(pi)  # numpy float has extra functionality ...
b.nbytes  # ... like the number of bytes it takes
binary_repr(b.view('u8'))  # view float number as an 8 byte integer, then get binary bitstring
