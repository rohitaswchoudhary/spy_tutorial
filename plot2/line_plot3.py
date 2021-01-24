import matplotlib.pyplot as plt
import numpy as np

a = np.array([[8,-1],[4,9]])
b = np.array([9,7])
c = np.linalg.solve(a,b)

plt.figure()

# Set x-axis range
plt.xlim((-10,10))
# Set y-axis range
plt.ylim((-10,10))
# Draw lines to split quadrants
plt.plot([-10, 10], [0, 0], color='C0')
plt.plot([0, 0], [-10, 10], color='C0')

# Draw line 8a-b=9 => b=8a-9
x = np.linspace(-10, 10)
y = 8 * x - 9
plt.plot(x, y, color='C2')

# Draw line 4a+9b=7 => b=(7-4a)/9
y = (7 - 4*x) / 9
plt.plot(x, y, color='C2')

# Add solution
plt.scatter(c[0], c[1], marker='x', color='black')
# Annotate solution
plt.annotate('({:0.3f}, {:0.3f})'.format(c[0], c[1]), c+0.5)

plt.title('Quadrant plot')

plt.show()