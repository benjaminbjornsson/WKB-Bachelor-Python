import numpy
import pylab
from Potential import *

alpha = 0.529
beta = 27.211

r = numpy.linspace(0.0, 30.0/alpha, 1000)

V = Dielectric(0, 5.0/beta, 5.01/alpha, 4.4)

pylab.figure(1)

V_data_plot = []

for argument in r:
	V_data_plot.append(beta*V(argument))

r = numpy.linspace(0.0, 30.0, 1000)
pylab.plot(r, V_data_plot)
pylab.savefig('testPlot')
