import numpy
import matplotlib
import matplotlib.pyplot

from Coulombic import *

import matplotlib.font_manager

font = {'family' : 'serif',
        'serif'  : ['Computer Modern Roman'],
        'size'   : 16}

matplotlib.rc('font', **font)
matplotlib.rc('font', weight='bold')
matplotlib.rc('text', usetex=True)

test = 10.0

x = numpy.linspace(0.0, 25.0 - test, int(1e5))

Energy = 0.1

l = 0
V_0 = -0.025
R = 2.0

V = Coulombic(l, V_0, R)

searchRange = [R, R + 15.0]
slope = -1
epsilon = 1e-8

xIntersect = numpy.array([R])

xIntersect = numpy.append(xIntersect, V.getIntersect(Energy, searchRange, slope, epsilon))

fig, ax = matplotlib.pyplot.subplots()

ax.plot(x, V(x), zorder = 0)

matplotlib.pyplot.scatter(xIntersect, Energy*numpy.ones(shape=xIntersect.shape), s = 10, c = 'black')
#matplotlib.pyplot.scatter(x_intersect, 2.0*numpy.ones(shape=x_intersect.shape), s = 10, c = 'black')

matplotlib.pyplot.hlines(Energy, 0.0, 25.0 - test, linestyles = 'solid')

matplotlib.pyplot.xlim(-1, 26.0 - test)
matplotlib.pyplot.ylim(-0.1, 0.6)

matplotlib.pyplot.xticks((xIntersect[0] , xIntersect[1], 24.5 - test), ('\it{r}_1', '\it{r}_2', '$\it{r}$'))
matplotlib.pyplot.yticks((-V_0, Energy, 0.53) ,('\it{V_0}', '\it{E}', '$\it{V}$($\it{r}$)'))

ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.spines["left"].set_position(('data', 0))
ax.spines["bottom"].set_position(('data', 0))

ax.arrow(-1, 0, 25.5 - test, 0, head_width = 0.02, head_length = 0.4, fc = 'k')
ax.arrow(0, -0.05, 0, 0.58, head_width = 0.4, head_length = 0.02, fc = 'k')

#matplotlib.pyplot.savefig('Coulomb_barrier.png', dpi = 300)

matplotlib.pyplot.show()
