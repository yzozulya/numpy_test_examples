from numpy import *

hypot(3., 4.)  # hypotenuse: sqrt(3**2 + 4**2) = 5
z = array([2 + 3j, 3 + 4j])
hypot(z.real, z.imag)  # norm of complex numbers
