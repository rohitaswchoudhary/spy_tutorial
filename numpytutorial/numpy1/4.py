# NumPy - Broadcasting

import numpy as np


a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print(c)

d = a*2
print(d)

x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3,4))

print(x.shape)
print(y.shape)


# print(x+y)  >> ValueError: operands could not be broadcast together with shapes (4,) (5,)

print(xx.shape)

print((xx+y).shape)

print("\n\n\n",xx+y)

print("                                               ")

print(x+z)
