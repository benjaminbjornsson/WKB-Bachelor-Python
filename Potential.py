class Potential(object):
	pass

class CoulombCentrifugalBarrier(Potential):
	def __init__(self, l, V_0, R):
		self.angularQNum = l
		self.trapPotential = V_0
		self.shellRadius = R

	def getAngularQNum(self):
		return self.angularQNum

	def getTrapPotential(self):
		return -self.trapPotential

	def getShellRadius(self):
		return self.shellRadius

class Coulombic(CoulombCentrifugalBarrier):
	def __init__(self, l, V_0, R):
		CoulombCentrifugalBarrier.__init__(self, l, V_0, R)

	def __call__(self, r):
		l = self.getAngularQNum()
		R = self.getShellRadius()
		if r > R:
			V = 1/r + l*(l+1)/(2*r**2)
		else:
			V = self.getTrapPotential()
		return V

class Dielectric(CoulombCentrifugalBarrier):
	def __init__(self, l, V_0, R, epsilon):
		CoulombCentrifugalBarrier.__init__(self, l, V_0, R)
		self.epsilon = epsilon

	def getEpsilon(self):
		return self.epsilon

	def __call__(self, r):
		l = self.getAngularQNum()
		R = self.getShellRadius()
		epsilon = self.getEpsilon()
		if r > R:
			V = -((epsilon + 1)*R**3)/(2*(epsilon + 2)*r**2*(r**2 - R**2)) + 1/r + l*(l+1)/(2*r**2)
		else:
			V = self.getTrapPotential()
		return V
