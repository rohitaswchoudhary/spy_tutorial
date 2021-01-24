import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy.core.defchararray import title

# Data for plotting
t=np.arange(0.0,2.0,0.01)
s=1+ np.sin(2*np.pi*t)

fig, ax = plt.subplots()
ax.plot(t,s,linewidth=0.5)
ax.set(xlabel='time(in s)', ylabel='voltage(in mV)',title='sinosidal voltage vs time plot')
ax.grid()
fig.savefig('line_plot_test.png')
plt.show()