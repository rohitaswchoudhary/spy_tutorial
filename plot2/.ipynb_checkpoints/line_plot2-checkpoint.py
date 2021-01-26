import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-100,100,100)

a=int(input("enter the coefficient of x: "))
b=int(input("enter the coefficient of y(other than 0): "))
c=int(input("enter the constant term: "))

y = a/b*x+c/b

plt.plot(x, y, '-r', label='ax+by+c=0')
plt.title('Graph of ax+by+c=0')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
