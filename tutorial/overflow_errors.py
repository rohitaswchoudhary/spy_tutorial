import numpy as np

print(np.power(100,8, dtype=np.int64))

print(np.power(100,8,dtype=np.int32))               #overflow error

print(np.iinfo(int))
print(np.iinfo(np.int32))
print(np.iinfo(np.int64))
print(np.iinfo(np.longlong))
print(np.iinfo(np.uint64))

print(np.power)