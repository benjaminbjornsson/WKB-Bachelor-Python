from CoulombCentrifugalBarrier import CoulombCentrifugalBarrier

class Coulombic(CoulombCentrifugalBarrier):
	def __init__(self, l, V_0, R):
		CoulombCentrifugalBarrier.__init__(self, l, V_0, R)

	def __call__(self, r):
		l = self.getAngularQuantumNum()
		R = self.getShellRadius()
		if r > R:
			V = 1/r + l*(l+1)/(2*r**2)
		else:
			V = self.getTrapPotential()
		return V
