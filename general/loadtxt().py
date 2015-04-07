from numpy import *

data = loadtxt("myfile.txt")  # myfile.txt contains 4 columns of numbers
t, z = data[:, 0], data[:, 3]  # data is 2D numpy array
t, x, y, z = loadtxt("myfile.txt", unpack=True)  # to unpack all columns
t, z = loadtxt("myfile.txt", usecols=(0, 3), unpack=True)  # to select just a few columns
data = loadtxt("myfile.txt", skiprows=7)  # to skip 7 rows from top of file
data = loadtxt("myfile.txt", comments='!')  # use '!' as comment char instead of '#'
data = loadtxt("myfile.txt", delimiter=';')  # use ';' as column separator instead of whitespace
data = loadtxt("myfile.txt", dtype=int)  # file contains integers instead of floats
