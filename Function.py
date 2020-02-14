import numpy

class Function(object):
    def __init__(self, UnitsOfFunction = None, UnitsOfVariables = None):
        self.UnitOfFunction = UnitsOfFunction
        self.UnitsOfVariables = UnitsOfVariables

    def plot(self, Range, NumberOfPoints = None, Axes = None, Title = None, xlable = None, ylabel = None):
        try:
            x = numpy.linspace(Range[0], Range[1], NumberOfPoints)
        except TypeError:
            x = numpy.linspace(Range[0], Range[1])

        f = self
        Axes.plot(x, f(x))
