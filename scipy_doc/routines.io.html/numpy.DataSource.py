import numpy as np

repos = DataSource()
repos.exists('www.google.com/index.html')
repos.exists('http://www.google.com/index.html')
ds = DataSource('/home/guido')
urlname = 'http://www.google.com/index.html'
gfile = ds.open('http://www.google.com/index.html')  # remote file
ds.abspath(urlname)
ds = DataSource(None)  # use with temporary file
ds.open('/home/guido/foobar.txt')
ds.abspath('/home/guido/foobar.txt')
