import matplotlib.pyplot as plt
import numpy as np

d=int(input('d: '))
e=int(input('e: '))
f=int(input('f: '))
g=int(input('g: '))
h=int(input('h: '))
i=int(input('i: '))

a = np.array([[d,e],[f,g]])
b = np.array([h,i])
c = np.linalg.solve(a,b)

plt.figure()

# Set x-axis range

plt.xlim((-10,10))

# Set y-axis range

plt.ylim((-10,10))

# Draw lines to split quadrants

plt.plot([-10, 10], [0, 0], color='C3')
plt.plot([0, 0], [-10, 10], color='C3')

# Draw line 8a-b=9 => b=8a-9

x = np.linspace(-10, 10)
y = (d * x - h)/e
plt.plot(x, y, color='C2')

# Draw line 4a+9b=7 => b=(7-4a)/9

y = (i - f*x) /g
plt.plot(x, y, color='C2')

# Add solution

plt.scatter(c[0], c[1], marker='o', color='black')

# Annotate solution

plt.annotate('({:0.3f}, {:0.3f})'.format(c[0], c[1]), c+0.5)

plt.title('Quadrant plot')

plt.show()