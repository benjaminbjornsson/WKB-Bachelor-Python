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

fig, ax = matplotlib.pyplot.subplots()

circle = matplotlib.patches.Circle((0, 0), radius = 5.0, facecolor = 'white', edgecolor = 'black')

ax.add_artist(circle)
matplotlib.pyplot.arrow(-5.0, 0.0, 35.0 - 0.5, 0.0, head_length = 0.5, head_width = 0.5, facecolor = 'black')
matplotlib.pyplot.arrow(0.0, 0.0, -(5 - 0.25)/numpy.sqrt(2), (5 - 0.25)/numpy.sqrt(2), head_length = 0.25, head_width = 0.25, facecolor = 'black')

matplotlib.pyplot.arrow(0.0, 0.0, 7.6, 7.4, head_length = 0.25, head_width = 0.25, facecolor = 'black')
matplotlib.pyplot.arrow(25.0, 0.0, -17.0, 7.5, head_length = 0.25, head_width = 0.25, facecolor = 'black')
matplotlib.pyplot.arrow(3.0, 0.0, 4.65, 7.4, head_length = 0.25, head_width = 0.25, facecolor = 'black')

chargeXPosition = (0.0, 3.0, 25.0)
chargeYPosition = (0.0, 0.0, 0.0)

matplotlib.pyplot.plot(chargeXPosition, chargeYPosition, '.k')


XPosition = (7.75, -5.0, 5.0)
YPosition = (7.6, 0.0, 0.0)

matplotlib.pyplot.plot(XPosition, YPosition, '.k')

matplotlib.pyplot.xlim(-5.5, 30.5)
matplotlib.pyplot.ylim(-7.5, 10.0)

ax.set_aspect(aspect = 1.0)

ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

matplotlib.pyplot.xticks((0.0, 3.0, 25.0), ('0', '\it{D}', '\it{x}'))
matplotlib.pyplot.yticks([])

ax.spines["bottom"].set_position(('data', 0))

matplotlib.pyplot.text(-1.9, 2.1, '\it{R}')

matplotlib.pyplot.text(0.0 - 0.25, 0.9, '\it{q_0}', fontsize = 13)
matplotlib.pyplot.text(3.0 - 0.5, 0.9, '\it{q_i}', fontsize = 13)
matplotlib.pyplot.text(25.0 - 0.25, 0.9, '\it{q}', fontsize = 13)

matplotlib.pyplot.text(4.0, 4.5, '\it{r_.}', fontsize = 15)
matplotlib.pyplot.text(6.75, 4.5, '\it{r_1}', fontsize = 15)
matplotlib.pyplot.text(15.0, 4.5, '\it{r_2}', fontsize = 15)

matplotlib.pyplot.text(5.25, 0.25, '\it{A}', fontsize = 15)
matplotlib.pyplot.text(-6.25, 0.25, '\it{B}', fontsize = 15)

#matplotlib.pyplot.show()

matplotlib.pyplot.savefig('conducting_sphere_potential.png', dpi = 300)
