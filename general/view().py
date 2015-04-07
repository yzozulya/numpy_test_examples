from numpy import *

a = array([1., 2.])
a.view()  # new array referring to the same data as 'a'
a.view(complex)  # pretend that a is made up of complex numbers
a.view(int)  # view(type) is NOT the same as astype(type)!
mydescr = dtype({'names': ['gender', 'age'], 'formats': ['S1', 'i2']})
a = array([('M', 25), ('F', 30)], dtype=mydescr)  # array with records
b = a.view(recarray)  # convert to a record array, names are now attributes
a['age']  # works with 'a' but not with 'b'
b.age  # works with 'b' but not with 'a'
