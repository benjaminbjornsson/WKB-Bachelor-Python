import numpy
import matplotlib.pyplot

class Function(object):
    def __init__(self, UnitsOfFunction = None, UnitsOfVariables = None):
        self.UnitOfFunction = UnitsOfFunction
        self.UnitsOfVariables = UnitsOfVariables

    def plot(self, Range, fig, NumberOfPoints = None, Units = None, Title = None, xlable = None, ylabel = None):
        f = self
        try:
            x = numpy.linspace(Range[0], Range[1], NumberOfPoints)
        except TypeError:
            x = numpy.linspace(Range[0], Range[1])
        
        alpha = 0.529
        beta = 27.211
        if Units != None:
            if Units[0] == 'Angstrom':
                self.alpha = 0.529
            if Units[1] == 'eV':
                self.beta = 27.211
        matplotlib.pyplot.plot(self.alpha*x, self.beta*f(x))
