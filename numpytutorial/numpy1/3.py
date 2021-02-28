# INDEXING AND SLICING

import numpy as np


data = np.array([1, 2, 3])

print(data[1])

print(data[0:2])

print(data[1:])

print(data[-2:])

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)

print(a[a<=10])

print(a[a>=6])

divisible_by_2 = a[a%2==0]

print(divisible_by_2)

c = a[(a>2)&(a<11)]
print(c)

five_up = (a>5)|(a==5)

print(five_up)

d = np.nonzero(a<5)
print(d)

print(a[d])

list_of_coordinates= list(zip(d[0], d[1]))

for coord in list_of_coordinates:
    print(coord)


# If the element you’re looking for doesn’t exist in the array, 
# then the returned array of indices will be empty. For example:

not_there = np.nonzero(a == 42)
print(not_there)

e = np.arange(10)**3

print(e)


for i in e:
    print(i**(1/3.))    


# Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:

def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)

print(b)

c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                 [ 10, 12, 13]],
                [[100,101,102],
                 [110,112,113]]])


print(c.shape)

print(c[1,...])                                   # same as c[1,:,:] or c[1]

print(c[...,2])                                   # same as c[:,:,2]




# Iterating over multidimensional arrays is done with respect to the first axis:

for row in b:
    print(row)

for element in b.flat:
    print(element)    





