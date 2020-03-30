import numpy
import matplotlib
import matplotlib.pyplot

import matplotlib.font_manager

font = {'family' : 'serif',
        'serif'  : ['Computer Modern Roman'],
        'size'   : 16}

matplotlib.rc('font', **font)
matplotlib.rc('font', weight='bold')
matplotlib.rc('text', usetex=True)


import scipy.optimize
x = numpy.linspace(0.1, 11.0, int(1e5))

V = lambda x : (1/x + 2*(x - 1)**4 - 1.0)*numpy.exp(-x) + 0.5

f = lambda x : V(x) - 2.0

x_0 = [0.5, 2.0, 6.0]
x_intersect = numpy.array([])
for arg in x_0:
    x_intersect = numpy.append(x_intersect, scipy.optimize.root(f, arg).x)

fig, ax = matplotlib.pyplot.subplots()

ax.plot(x, V(x), zorder = 0)

matplotlib.pyplot.scatter(x_intersect, 2.0*numpy.ones(shape=x_intersect.shape), s = 10, c = 'black')

matplotlib.pyplot.vlines(x_intersect[0], 0.0, 2.0, linestyles = 'dashed', zorder = 1)
matplotlib.pyplot.vlines(x_intersect[1], 0.0, 2.0, linestyles = 'dashed')
matplotlib.pyplot.vlines(x_intersect[2], 0.0, 2.0, linestyles = 'dashed')

matplotlib.pyplot.hlines(2.0, 0.0, 11.0, linestyles = 'solid')

matplotlib.pyplot.xlim(-1, 11.0)
matplotlib.pyplot.ylim(-1, 6.5)

matplotlib.pyplot.xticks(numpy.append(x_intersect, 10.5), ('\it{a}', '\it{b}', '\it{c}', '$\it{x}$'))
matplotlib.pyplot.yticks((2.0, 6.0) ,('\it{E}', '$\it{V}$($\it{x}$)'))

ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.spines["left"].set_position(('data', 0))
ax.spines["bottom"].set_position(('data', 0))

ax.arrow(-1, 0, 11.5, 0, head_width = 0.2, head_length = 0.2, fc = 'k')
ax.arrow(0, -1, 0, 7, head_width = 0.2, head_length = 0.2, fc = 'k')

arrow_x = numpy.linspace(0.9, 2.6, int(1e4))
arrow_y = 3.0 + 0.05*numpy.sin(2*numpy.pi*arrow_x/(6.0/13.0))

ax.plot(arrow_x, arrow_y, 'k')
ax.plot(2.6, 3.0, marker = (3, 0, -90), markerfacecolor = 'black', markeredgecolor = 'black', markersize = 8)

arrow_y = 2.5 + 0.05*numpy.sin(2*numpy.pi*arrow_x/(6.0/13.0))

ax.plot(arrow_x, arrow_y, 'k')
ax.plot(0.9, 2.5, marker = (3, 0, 90), markerfacecolor = 'black', markeredgecolor = 'black', markersize = 8)

arrow_x = numpy.linspace(8.4, 10, int(1e4))
arrow_y = 2.5 + 0.05*numpy.sin(2*numpy.pi*arrow_x/(6.0/13.0))

ax.plot(arrow_x, arrow_y, 'k')
ax.plot(10, 2.5, marker = (3, 0, -90), markerfacecolor = 'black', markeredgecolor = 'black', markersize = 8)

#matplotlib.pyplot.savefig('WKB_turningpoints.png', dpi = 300)

matplotlib.pyplot.show()
