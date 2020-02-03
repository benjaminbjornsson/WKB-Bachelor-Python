import numpy

from Potential import Potential

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
	
	def getIntersect(self, Energy, searchRange, slopeSign, epsilon):
		return self.bisectionSearch(Energy, searchRange, slopeSign, epsilon)

	def bisectionSearch(self, Energy, searchRange, slopeSign, epsilon):
		lowerLimit = searchRange[0]
		higherLimit = searchRange[1]
		midValue = (lowerLimit + higherLimit)/2.0
		V = self
		while numpy.abs(V(midValue) - Energy) > epsilon:
#			print([lowerLimit, midValue, higherLimit, V(lowerLimit), V(midValue), V(higherLimit)])
			if V(midValue) > Energy:
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
		if (V(midValue) - Energy) < 0:
			if slopeSign < 0:
				alpha = 0.99
				while V(lowerLimit + alpha*(midValue - lowerLimit)) < Energy:
					alpha = alpha**2
				midValue = lowerLimit + alpha*(midValue - lowerLimit)
			else:
				alpha = 0.99
				while V(higherLimit - alpha*(higherLimit - midValue)) < Energy:
					alpha = alpha**2
				midValue = higherLimit - alpha*(higherLimit - midValue)
		return midValue

	def __call__(self, r):
		raise NotImplementedError("This function should be implemented by a child class")
