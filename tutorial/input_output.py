import numpy as np

from io import StringIO

data = u"1, 2, 3\n4, 5, 6"

print(np.genfromtxt(StringIO(data), delimiter=","))

data1 = u"  1  2  3\n  4  5 67\n890123  4"
print(np.genfromtxt(StringIO(data1), delimiter=3))

data2 = u"123456789\n   4  7 9\n   4567 9"
print(np.genfromtxt(StringIO(data2), delimiter=(4, 3, 2)))

# The comments argument

data3 = u"""#
# Skip me !
# Skip me too !
1, 2
3, 4
5, 6 #This is the third line of the data
7, 8
# And here comes the last line
9, 0
"""
print(np.genfromtxt(StringIO(data3), comments="#", delimiter=","))