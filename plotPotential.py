import numpy
import pylab
from Coulombic import Coulombic
from Dielectric import Dielectric

alpha = 0.529
beta = 27.211

r = numpy.linspace(0.0, 75.0/alpha, 1e6)

V = Dielectric(0, 0.5/beta, 5.01/alpha, 4.4)

pylab.figure(1)

V_data_plot = []

for argument in r:
	V_data_plot.append(beta*V(argument))

r = numpy.linspace(0.0, 75.0, 1e6)
pylab.plot(r, V_data_plot)
r_pos_intersect_1 = alpha*V.getIntersect(0.3/beta, [5.0/alpha, 7.0/alpha], 1, 1e-7)
r_pos_intersect_2 = alpha*V.getIntersect(0.3/beta, [7.0/alpha, r[-1]/alpha], -1, 1e-7)
pylab.plot([r[0], r[-1]], [0.3, 0.3])
pylab.plot([r_pos_intersect_1, r_pos_intersect_2], [0.3, 0.3], 'x')
pylab.xlabel('r [Å]')
pylab.ylabel('V(r) [eV]')
pylab.savefig('testPlot')


