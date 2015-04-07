from numpy import *

f = finfo(float)  # the numbers given are machine dependent
f.nmant, f.nexp  # nr of bits in the mantissa and in the exponent
f.machep  # most negative n so that 1.0 + 2**n != 1.0
f.eps  # floating point precision: 2**machep
f.precision  # nr of precise decimal digits: int(-log10(eps))
f.resolution  # 10**(-precision)
f.negep  # most negative n so that 1.0 - 2**n != 1.0
f.epsneg  # floating point precision: 2**negep
f.minexp  # most negative n so that 2**n gives normal numbers
f.tiny  # smallest usuable floating point nr: 2**minexp
f.maxexp  # smallest positive n so that 2**n causes overflow
f.min, f.max  # the most negative and most positive usuable floating number
