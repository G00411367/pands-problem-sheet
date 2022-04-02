# This program plots functions f(x)=x, g(x)=x^2 and h(x)=x^3
# in the range [0,4]
# Author Ioan Domsa

import numpy as np
import matplotlib.pyplot as plt
step = 0.25 # set a calculation step for the plot to be smoother 
xpoints = np.arange(0, 5, step)

# define the functions f(x), g(x) and h(x)
fx = xpoints
gx = np.power(xpoints, 2)
hx = np.power(xpoints, 3)
# plot functions with different colours

plt.plot(xpoints, fx, label = "f(x)", color = "b")
plt.plot(xpoints, gx, label = "g(x)", color = "m")
plt.plot(xpoints, hx, label = "h(x)", color = "r")
# add elements to plot: title, labels, etc. 
plt.title("Plots \n f(x)=x, g(x)=x\u00b2, h(x)=x\u00b3")
plt.xlabel("X"); plt.ylabel("f(x), g(x), h(x)")
plt.legend(loc="upper left")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plot start from 0,0
plt.margins(0)
plt.savefig('Task08-plot.png')

