from CoulombCentrifugalBarrier import CoulombCentrifugalBarrier
import numpy

class Metallic(CoulombCentrifugalBarrier):
    def __init__(self, angularQuantumNumber, V_0, shellRadius, UnitsOfFunction = None, UnitsOfVariables = None):
        CoulombCentrifugalBarrier.__init__(self, angularQuantumNumber, V_0, shellRadius, UnitsOfFunction, UnitsOfVariables)
        self.delta = 0.0
        self.delta = self.bisectionSearch(self.getTrapPotential(), [shellRadius, 3.0 + shellRadius], 1, 1e-9) - shellRadius

    def getDelta(self):
        return self.delta

    def getValue(self, r): 
        l = self.getAngularQuantumNum()
        R = self.getShellRadius()
        delta = self.getDelta()
        if r > R + delta:
            V = -(R**3)/(2*r**2*(r**2 - R**2)) + 1/r + l*(l + 1)/(2*r**2)
            V = -(R**3)/(r**2*(r**2 - R**2)) + 1/r + l*(l + 1)/(2*r**2)
        else:
            V = self.getTrapPotential()
        return V

    def __call__(self, r):
        if isinstance(r, numpy.ndarray):
            Varray = numpy.vectorize(self.getValue)
            return Varray(r)
        else:
            return self.getValue(r)
