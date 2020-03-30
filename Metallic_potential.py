import numpy
import matplotlib
import matplotlib.pyplot

import matplotlib.font_manager

from Metallic import *
from Coulombic import *

font = {'family' : 'serif',
        'serif'  : ['Computer Modern Roman'],
        'size'   : 16}

matplotlib.rc('font', **font)
matplotlib.rc('font', weight='bold')
matplotlib.rc('text', usetex=True)

angularQuantumNumber = [0, 1, 2, 3]
V_0 = 0.02
R_0 = 8.0

V_list = []
for l in angularQuantumNumber:
    V_list.append(Metallic(l, V_0, R_0))

V_list.append(Coulombic(0, V_0, R_0))

x = numpy.linspace(0.0, 100.0, int(1e5))

fig, ax = matplotlib.pyplot.subplots()

for V in V_list:
    if isinstance(V, Metallic):
        ax.plot(x, V(x))
    else:
        ax.plot(x, V(x), ':k')

matplotlib.pyplot.xlim(-10, 70.0)
matplotlib.pyplot.ylim(-0.03, 0.125)

matplotlib.pyplot.xticks((R_0, 70.0 - 1.5), ('', '$x$'))
matplotlib.pyplot.yticks((-V_0, 0.125 - 0.004) ,('$V_0$', '$V(x)$'))

ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.spines["left"].set_position(('data', 0))
ax.spines["bottom"].set_position(('data', 0))

ax.arrow(-10, 0, 80.0, 0, width = 0.00025, head_width = 0.004, head_length = 1.5, fc = 'k', length_includes_head = True)
ax.arrow(0, -0.025, 0, 0.15, head_width = 1.5, head_length = 0.004, fc = 'k', length_includes_head = True)

matplotlib.pyplot.text(R_0 - 4.0, -0.009, '$R_0$', fontsize = 15)

ax.arrow(55.0, 0.0875 - 0.003, 10.0, 0, width = 0.0015, head_width = 0, head_length = 0, facecolor = 'C0', edgecolor = 'white')
ax.arrow(55.0, 0.095 - 0.002, 10.0, 0, width = 0.0015, head_width = 0, head_length = 0, facecolor = 'C1', edgecolor = 'white')
ax.arrow(55.0, 0.1025 - 0.001, 10.0, 0, width = 0.0015, head_width = 0, head_length = 0, facecolor = 'C2', edgecolor = 'white')
ax.arrow(55.0, 0.11, 10.0, 0, width = 0.0015, head_width = 0, head_length = 0, facecolor = 'C3', edgecolor = 'white')

matplotlib.pyplot.text(55.0, 0.111 + 0.0005, '$\mathbf{\ell} = 3$', fontsize = 12)
matplotlib.pyplot.text(55.0, 0.1035 - 0.0005, '$\ell = 2$', fontsize = 12)
matplotlib.pyplot.text(55.0, 0.096 - 0.0015, '$\ell = 1$', fontsize = 12)
matplotlib.pyplot.text(55.0, 0.0885 - 0.0025, '$\ell = 0$', fontsize = 12)

matplotlib.pyplot.savefig('Metallic_potential.png', dpi = 300)

#matplotlib.pyplot.show()
