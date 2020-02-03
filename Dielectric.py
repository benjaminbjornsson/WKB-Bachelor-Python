from CoulombCentrifugalBarrier import CoulombCentrifugalBarrier

class Dielectric(CoulombCentrifugalBarrier):
	def __init__(self, l, V_0, R, dielectricConstant):
		CoulombCentrifugalBarrier.__init__(self, l, V_0, R)
		self.dielectricConstant = dielectricConstant
		self.delta = 0.0
		self.delta = self.bisectionSearch(self.getTrapPotential(), [R, R + 2.0], 1, 1e-7) - R

	def getDielectricConstant(self):
		return self.dielectricConstant

	def getDelta(self):
		return self.delta

	def __call__(self, r):
		l = self.getAngularQuantumNum()
		R = self.getShellRadius()
		delta = self.getDelta()
		dielectricConstant = self.getDielectricConstant()
		if r > R + delta:
			V = -((dielectricConstant - 1)*R**3)/(2*(dielectricConstant + 2)*r**2*(r**2 - R**2)) + 1/r + l*(l+1)/(2*r**2)
		else:
			V = self.getTrapPotential()
		return V
