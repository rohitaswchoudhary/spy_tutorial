import numpy as np
from numpy.core.fromnumeric import reshape


# numpy ndarray object

a = np.array([1,2,3])
print(a)

a1 = np.array([[1,2,3],[4,5,6]])
print("\n",a1)

# ndnimm parameter

a2 = np.array([1,2,3,4,5,6],ndmin=2)
print(a2)

# dtype parameter 

a3 = np.array([1,2,3],dtype=complex) 
print(a3)

# ndarray.shape attribute
# This array attribute returns a tuple consisting of array dimensions. It can also be used to resize the array.

print(a1.shape)

# reshape

a1.shape=(3,2)
print(a1)

b1 = a1.reshape(3,2)
print(b1)


# ndarray.ndim
# This array attribute returns the number of array dimensions.

print("\n",a1.ndim)

# numpy.itemsize
# This array attribute returns the length of each element of array in bytes.

print(a1.itemsize)

# numpy.flags
# The ndarray object has the following attributes. Its current values are returned by this function.

x = np.array([1,2,3,4,5]) 
print(x.flags)

# numpy.empty
# It creates an uninitialized array of specified shape and dtype. It uses the following constructor −

x1 = np.empty([3,2], dtype = int) 
print(x1)

x2 = np.ones([2,2], dtype = int) 
print("\n",x2)

# numpy.asarray
# This function is similar to numpy.array except for the fact that it has fewer parameters. 
# This routine is useful for converting Python sequence into ndarray.

x3 = [1,2,3]

print("\n",np.asarray(x3))

x4 = (1,2,3)
print("\n",np.asarray(x4))

# numpy.frombuffer
# This function interprets a buffer as one-dimensional array. 
# Any object that exposes the buffer interface is used as parameter to return an ndarray.

s = b'Hello World' 
print("\n",np.frombuffer(s,dtype='S1'))


# numpy.fromiter
# This function builds an ndarray object from any iterable object. 
# A new one-dimensional array is returned by this function.

list= range(1,5)
print(list)

it = iter(list)  

print(np.fromiter(it, dtype = float))

# numpy.arange
# This function returns an ndarray object containing evenly spaced values within a given range. 
# The format of the function is as follows −

# numpy.arange(start, stop, step, dtype)

x5 = np.arange(10,50,2,dtype=int)

print(x5)

# numpy.linspace
# This function is similar to arange() function. In this function, instead of step size, 
# the number of evenly spaced values between the interval is specified. The usage of this function is as follows −

x6  = np.linspace(10,20,5)
print(x6)

x7 = np.linspace(10,20,5,endpoint=False,retstep=True)
print(x7)


# numpy.logspace
# This function returns an ndarray object that contains the numbers that are evenly spaced on a log scale. 
# Start and stop endpoints of the scale are indices of the base, usually 10.

# numpy.logspace(start, stop, num, endpoint, base, dtype)

x8 = np.logspace(1.0, 2.0, num = 10) 
print(x8)

x9 = np.logspace(1,10,num=10,base=2)
print(x9)