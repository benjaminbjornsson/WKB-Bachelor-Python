from CoulombCentrifugalBarrier import CoulombCentrifugalBarrier
import numpy

class Dielectric(CoulombCentrifugalBarrier):
    def __init__(self, l, V_0, R, dielectricConstant, UnitsOfFunction = None, UnitsOfVariables = None):
        CoulombCentrifugalBarrier.__init__(self, l, V_0, R, UnitsOfFunction, UnitsOfVariables)
        self.dielectricConstant = dielectricConstant
        self.delta = 0.0
        self.delta = self.bisectionSearch(self.getTrapPotential(), [R, R + 2.0], 1, 1e-10) - R

    def getDielectricConstant(self):
        return self.dielectricConstant

    def getDelta(self):
        return self.delta

    def getValue(self, r): 
        l = self.getAngularQuantumNum()
        R = self.getShellRadius()
        delta = self.getDelta()
        dielectricConstant = self.getDielectricConstant()
        if r > R + delta:
            V = -((dielectricConstant - 1)*R**3)/(2*(dielectricConstant + 2)*r**2*(r**2 - R**2)) + 1/r + l*(l+1)/(2*r**2)
        else:
            V = self.getTrapPotential()
        return V

    def __call__(self, r):
        if isinstance(r, numpy.ndarray):
            Varray = numpy.vectorize(self.getValue)
            return Varray(r)
        else:
            return self.getValue(r)
