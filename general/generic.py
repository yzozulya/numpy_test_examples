from numpy import *

numpyscalar = string_('7')  # Convert to numpy scalar

numpyscalar  # Looks like a build-in scalar...
type(numpyscalar)  # ... but it isn't
buildinscalar = '7'  # Build-in python scalar
type(buildinscalar)
isinstance(numpyscalar, generic)  # Check if scalar is a NumPy one
isinstance(buildinscalar, generic)  # Example on how to recognize NumPy scalars

int_
bool_
float_
cfloat
string_
unicode_
void
object_