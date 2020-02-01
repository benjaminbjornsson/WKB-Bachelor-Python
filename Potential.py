class Potential(object):
	pass

class CoulombCentrifugalBarrier(Potential):
	def __init__(self, l, V_0, R):
		self.angularQuantumNum = l
		self.trapPotential = V_0
		self.shellRadius = R

	def getAngularQuantumNum(self):
		return self.angularQuantumNum

	def getTrapPotential(self):
		return -self.trapPotential

	def getShellRadius(self):
		return self.shellRadius

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

class Dielectric(CoulombCentrifugalBarrier):
	def __init__(self, l, V_0, R, delta, dielectricConstant):
		CoulombCentrifugalBarrier.__init__(self, l, V_0, R)
		self.dielectricConstant = dielectricConstant
		self.delta = delta

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
