import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(-10, 10, 0.01) # between -10 and 10, 0.01 stepsize
y1 = 8*x1-9

x2 = np.arange(-10, 10, 0.01) # between -10 and 10, 0.01 stepsize
y2 = (7-4*x2)/9

plt.figure()
# Set x-axis range
plt.xlim((-10,10))
# Set y-axis range
plt.ylim((-10,10))
# Draw lines to split quadrants
plt.plot([-10,-10],[10,10], linewidth=4, color='blue' )
plt.plot(x1,y1)
plt.plot(x2,y2)

#draw the equations
# plt.plot(x1[0][0],x1[0][1], linewidth=2, color='red' )
# plt.plot(x2[1][0],x2[1][1], linewidth=2, color='red' )

# plt.plot(c[0],c[1], marker='x', color="black")

plt.title('Quadrant plot')

plt.show()