from numpy import *

data = array([[1, 2], [3, 4]])
x = array([1, 2])
y = array([1, 2])
savetxt("myfile.txt", data)  # data is 2D array
savetxt("myfile.txt", x)  # x is 1D array. 1 column in file.
savetxt("myfile.txt", (x, y))  # x,y are 1D arrays. 2 rows in file.
savetxt("myfile.txt", transpose((x, y)))  # x,y are 1D arrays. 2 columns in file.
savetxt("myfile.txt", transpose((x, y)), fmt='%6.3f')  # use new format instead of '%.18e'
savetxt("myfile.txt", data, delimiter=';')  # use ';' to separate columns instead of space
