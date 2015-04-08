import numpy as np

charar = np.chararray((3, 3))
charar[:] = 'a'
charar

charar = np.chararray(charar.shape, itemsize=5)
charar[:] = 'abc'
charar

dtype = np.int8
charar.astype(dtype)
charar.argsort()
charar.copy()

sub = '1'
charar.count(sub)
charar.decode()
charar.dump(file)
charar.dumps()
charar.encode()

suffix = ''
charar.endswith(suffix)
charar.expandtabs()

value = ''
charar.fill(value)
charar.find(sub)
charar.flatten()
charar.getfield(dtype)
charar.index(sub)
charar.isalnum()
charar.isalpha()
charar.isdecimal()
charar.isdigit()
charar.islower()
charar.isnumeric()
charar.isspace()
charar.istitle()
charar.isupper()
charar.item()

seq = [1, 2, 3]
charar.join(seq)

width = 1
charar.ljust(width)

charar.lower()
charar.lstrip()
charar.nonzero()

indices = [1, 3]
values = [1, 2, 3, 4]
charar.put(indices, values)
charar.ravel()

repeats = 1
charar.repeat(repeats)

old = '1'
new = '2'
charar.replace(old, new)

shape = (1, 2)
charar.reshape(shape)
charar.resize(shape)
charar.rfind(sub)
charar.rindex(sub)
charar.rjust(width)
charar.rsplit()
charar.rstrip()

v = 1
charar.searchsorted(v)

val = 1
charar.setfield(val, dtype)

charar.setflags()
charar.sort()
charar.split()
charar.splitlines()
charar.squeeze()

prefix = ''
charar.startswith(prefix)
charar.strip()

charar.swapaxes(1, 2)
charar.swapcase()
charar.take(indices)
charar.title()

fid = open('')
charar.tofile(fid)
charar.tolist()
charar.tostring()

table = [1, 2]
charar.translate(table)
charar.transpose()
charar.upper()
charar.view()
charar.zfill(width)