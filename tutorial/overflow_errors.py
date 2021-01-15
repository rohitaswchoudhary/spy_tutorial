import numpy as np

print(np.power(100,8, dtype=np.int64))

print(np.power(100,8,dtype=np.int32))               #overflow error

print(np.iinfo(int))
print(np.iinfo(np.int32))
print(np.iinfo(np.int64))
print(np.iinfo(np.longlong))
print(np.iinfo(np.uint64))

print(np.power)

x = np.array([[1,3,0], [-1,2,1], [0, 0, 2]])
y = np.matrix([[2, 3, 4], [1,2,3], [-1,1,2]])
print(np.dot(x, y))
print(np.dot(y, x))