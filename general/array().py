from numpy import *

array([1, 2, 3])  # conversion from a list to an array
array([1, 2, 3], dtype=complex)  # output type is specified
array(1, copy=0, subok=1, ndmin=1)  # basically equivalent to atleast_1d
array(1, copy=0, subok=1, ndmin=2)  # basically equivalent to atleast_2d
array(1, subok=1, ndmin=2)  # like atleast_2d but always makes a copy
mydescriptor = {'names': ('gender', 'age', 'weight'),
                'formats': ('S1', 'f4', 'f4')}  # one way of specifying the data type
a = array([('M', 64.0, 75.0), ('F', 25.0, 60.0)], dtype=mydescriptor)  # recarray
print a
a['weight']
a.dtype.names  # Access to the ordered field names
mydescriptor = [('age', int16), ('Nchildren', int8), ('weight', float32)]  # another way of specifying the data type
a = array([(64, 2, 75.0), (25, 0, 60.0)], dtype=mydescriptor)
a['Nchildren']
mydescriptor = dtype([('x', 'f4'), ('y', 'f4'),  # nested recarray
                      ('nested', [('i', 'i2'), ('j', 'i2')])])
array([(1.0, 2.0, (1, 2))], dtype=mydescriptor)  # input one row
array([(1.0, 2.0, (1, 2)), (2.1, 3.2, (3, 2))], dtype=mydescriptor)  # input two rows
a = array([(1.0, 2.0, (1, 2)), (2.1, 3.2, (3, 2))], dtype=mydescriptor)  # getting some columns
a['x']  # a plain column
a['nested']  # a nested column
a['nested']['i']  # a plain column inside a nested column
mydescriptor = dtype([('x', 'f4'), ('y', 'f4'),  # nested recarray
                      ('nested', [('i', 'i2'), ('j', 'i2')])])
array([(1.0, 2.0, (1, 2))], dtype=mydescriptor)  # input one row
array([(1.0, 2.0, (1, 2)), (2.1, 3.2, (3, 2))], dtype=mydescriptor)  # input two rows
a = array([(1.0, 2.0, (1, 2)), (2.1, 3.2, (3, 2))], dtype=mydescriptor)  # getting some columns
a['x']  # a plain column
a['nested']  # a nested column
a['nested']['i']  # a plain column inside a nested column
