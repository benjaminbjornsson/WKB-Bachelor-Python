import numpy
import pylab
import scipy.integrate
from Dielectric import Dielectric

gamma = 1e-8
dielectricConstant = 4.4
angularQuantumNumber = range(0, 3)
alpha = 0.529
beta = 27.211
V_0 = 0.5/beta
timeConversionFactor = 2.419*1e-17

R_0 = 3.55/alpha
DeltaR = 1.46/alpha

def shellRadius(N):
	return numpy.sqrt(N)/numpy.sqrt(60)*R_0 + DeltaR

def Energy_Affinity_2(N):
	return (2.8521 - 15.7922/(alpha*shellRadius(N)))/beta

def kappa(r, V, Energy):
	return numpy.sqrt(2*(V(r) - Energy))

def tau(V, Energy, Range):
	f = numpy.exp(scipy.integrate.quad(kappa, Range[0], Range[1], args=(V, Energy), full_output = 0, epsabs=1e-10))
	Tr = 4/(2*f + 1/(2*f))**2
	vinc = numpy.sqrt(2*Energy)
	return (2*(V.getShellRadius() + V.getDelta()))/(Tr*vinc)

NList = [20, 40, 60, 64, 68, 70, 74, 78, 82, 84, 86, 88, 90]

for N in NList:
	pylab.figure()
	if -1/Energy_Affinity_2(N) < 0:
		break
	intersectionRightList = numpy.array([])
	intersectionLeftList = numpy.array([])
	rangeRight = [shellRadius(N) + 2.0/alpha, -1/Energy_Affinity_2(N) + 10.0/alpha]
	rangeLeft = [0.0, shellRadius(N) + 2.0/alpha]
	Energy = -Energy_Affinity_2(N)
	PotentialList = []
	for l in angularQuantumNumber:
		PotentialList.append(Dielectric(l, V_0, shellRadius(N), dielectricConstant))
		intersectionRightList = numpy.append(intersectionRightList, [PotentialList[-1].getIntersect(Energy, rangeRight, -1, gamma)])
		intersectionLeftList = numpy.append(intersectionLeftList, [PotentialList[-1].getIntersect(Energy, rangeLeft, 1, gamma)])

	lifeTimes = []
	for l in angularQuantumNumber:
		lifeTimes.append(format(tau(PotentialList[l], Energy, [intersectionLeftList[l], intersectionRightList[l]])[0]*timeConversionFactor, '.1e'))

	print(lifeTimes)
	continue
#	r = numpy.linspace(0.0, numpy.max(intersectionRightList) + 10.0, 1e6)
#	PotentialValues = numpy.zeros(shape=(len(PotentialList), len(r)))

#	for i in range(0, len(PotentialList)):
#		for j in range(0, len(r)):
#			PotentialValues[i][j] = PotentialList[i](r[j])

#	kappaValues = numpy.zeros(shape=(len(PotentialList), len(r)))
#	for i in range(0, len(PotentialList)):
#		rprim = numpy.linspace(intersectionLeftList[i], intersectionRightList[i], len(r))
#		for j in range(0, len(rprim)):
#			kappaValues[i][j] = kappa(rprim[j], PotentialList[i], Energy)

#	for i in range(0, len(PotentialList)):
#		pylab.plot(alpha*r, beta*PotentialValues[i][:])	
#		rprim = numpy.linspace(intersectionLeftList[i], intersectionRightList[i], len(r))
#		pylab.plot(alpha*rprim, numpy.sqrt(beta)*kappaValues[i][:])
		

#	pylab.plot(alpha*intersectionRightList, -beta*Energy_Affinity_2(N)*numpy.ones(shape=numpy.shape(intersectionRightList)), 'x')
#	pylab.plot(alpha*intersectionLeftList, -beta*Energy_Affinity_2(N)*numpy.ones(shape=numpy.shape(intersectionLeftList)), 'x')
#	pylab.plot(alpha*numpy.array([r[0], r[-1]]), -beta*Energy_Affinity_2(N)*numpy.ones(shape=(2, 1)))
#	pylab.xlabel('r [Å]')
#	pylab.ylabel('V(r) [eV]')
#	pylab.savefig('testPlot' + str(int(N)))
#	print('intersectionLeftList: ' + str(alpha*intersectionLeftList))
#	print('intersectionRightList: ' + str(alpha*intersectionRightList))
