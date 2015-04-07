from numpy import *

a = array([5])
type(a[0])
a.item()  # Conversion of array of size 1 to Python scalar
type(a.item())
b = array([2, 3, 4])
b[1].item()  # Conversion of 2nd element to Python scalar
type(b[1].item())
b.item(2)  # Return 3rd element converted to Python scalar
type(b.item(2))
type(b[2])  # b[2] is slower than b.item(2), and there is no conversion
