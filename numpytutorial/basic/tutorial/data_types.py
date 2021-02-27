import numpy as np

x=np.int_([1,2,4])
print(x)

y=np.float32(x)
print(y)

z= np.array(3,dtype= np.uint8)
print(z)

print(np.array([1,2,3],dtype='f'))

# to convert type of an array, use the ".astype()" method(preferred) or the type itself as a function (np.int8(z)).

z.astype(float)
print(z.dtype)
print('rohit')
