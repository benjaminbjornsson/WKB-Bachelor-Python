import numpy
import pylab
from Potential import *

alpha = 0.529
beta = 27.211

r = numpy.linspace(0.0, 75.0/alpha, 1e6)

V = Dielectric(0, 0.5/beta, 5.01/alpha, 0.4/alpha, 4.4)

pylab.figure(1)

V_data_plot = []

for argument in r:
	V_data_plot.append(beta*V(argument))

r = numpy.linspace(0.0, 75.0, 1e6)
pylab.plot(r, V_data_plot)
pylab.xlabel('r [Å]')
pylab.ylabel('V(r) [eV]')
pylab.savefig('testPlot')

print(V_data_plot[-1])
