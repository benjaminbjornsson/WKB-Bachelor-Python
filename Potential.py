import numpy

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

	def bisectionSearch(self, E, searchRange, slopeSign, epsilon):
		lowerLimit = searchRange[0]
		higherLimit = searchRange[1]
		midValue = (lowerLimit + higherLimit)/2.0
		V = self
		while numpy.abs(V(midValue) - E) > epsilon:
#			print([lowerLimit, midValue, higherLimit, V(lowerLimit), V(midValue), V(higherLimit)])
			if V(midValue) > E:
				if slopeSign > 0:
					higherLimit = midValue
				else:
					lowerLimit = midValue
			else:
				if slopeSign > 0:
					lowerLimit = midValue
				else:
					higherLimit = midValue
			midValue = (lowerLimit + higherLimit)/2.0
		if (V(midValue) - E) < 0:
			if slopeSign < 0:
				alpha = 0.99
				while V(lowerLimit + alpha*(midValue - lowerLimit)) < E:
					alpha = alpha**2
				midValue = lowerLimit + alpha*(midValie - lowerLimit)
			else:
				alpha = 0.99
				while V(higherLimit - alpha*(higherLimit - midValue)) < E:
					alpha = alpha**2
				midValue = higherLimit - alpha*(higherLimit - midValue)
		return midValue
		

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
