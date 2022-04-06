# This displays a plot of the functions on the one set of axes
#author:Regina Fennessy


import numpy as np
import matplotlib.pyplot as plt

#f(x)=x, g(x)=x2 and h(x)=x3

#range [0, 4]
xpoints = np.array(range(0,4))

xpoints = xpoints

y1points = xpoints * xpoints

y2points = xpoints * xpoints *  xpoints

plt.plot(xpoints, xpoints, label = "X", color="Grey")
plt.plot(xpoints, y1points, label = "squared", color="black")
plt.plot(xpoints, y2points, label = "cubed", color="blue")



plt.legend()
plt.show()


