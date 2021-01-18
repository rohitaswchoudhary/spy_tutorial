import numpy as np

x = np.array([[1,3,0], [-1,2,1], [0, 0, 2]])
y = np.matrix([[2, 3, 4], [1,2,3], [-1,1,2]])
print(np.dot(x, y))
print(np.dot(y, x))

print(x==y)