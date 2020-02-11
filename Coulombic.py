from CoulombCentrifugalBarrier import CoulombCentrifugalBarrier
import numpy

class Coulombic(CoulombCentrifugalBarrier):
    def __init__(self, l, V_0, R, UnitsOfFunction = None, UnitsOfVariables = None):
        CoulombCentrifugalBarrier.__init__(self, l, V_0, R, UnitsOfFunction, UnitsOfVariables)

    def getValue(self, r, l, R):
        if r > R:
            V = 1/r + l*(l+1)/(2*r**2)
        else:
            V = self.getTrapPotential()
        return V

    def __call__(self, r):
        l = self.getAngularQuantumNum()
        R = self.getShellRadius()
        if isinstance(r, numpy.ndarray):
            Vfun = numpy.vectorize(self.getValue)
            return Vfun(r, l, R)
        else:
            return self.getValue(r, l, R)
