import numpy
import pylab
from Dielectric import Dielectric

gamma = 1e-7
dielectricConstant = 4.4
angularQuantumNumber = range(0, 3)
alpha = 0.529
beta = 27.211
V_0 = 0.5/beta

R_0 = 3.55/alpha
DeltaR = 1.46/alpha

def shellRadius(N):
	return numpy.sqrt(N)/numpy.sqrt(60)*R_0 + DeltaR

def Energy_Affinity_2(N):
	return (2.8521 - 15.7922/(alpha*shellRadius(N)))/beta

NList = [20, 40, 60, 64, 68, 70, 74, 78, 82, 84, 86, 88, 90]

for N in NList:
#	pylab.figure()
	if -1/Energy_Affinity_2(N) < 0:
		break
	intersectionRightList = numpy.array([])
	intersectionLeftList = numpy.array([])
	PotentialList = []
	for l in angularQuantumNumber:
		PotentialList.append(Dielectric(l, V_0, shellRadius(N), dielectricConstant))
		rangeRight = [shellRadius(N) + 2.0/alpha, -1/Energy_Affinity_2(N) + 10.0/alpha]
		rangeLeft = [0.0, shellRadius(N) + 2.0/alpha]
		Energy = -Energy_Affinity_2(N)
		intersectionRightList = numpy.append(intersectionRightList, [PotentialList[-1].getIntersect(Energy, rangeRight, -1, gamma)])
		intersectionLeftList = numpy.append(intersectionLeftList, [PotentialList[-1].getIntersect(Energy, rangeLeft, 1, gamma)])
#	r = numpy.linspace(0.0, numpy.max(intersectionRightList) + 10.0, 1e6)
#	PotentialValues = numpy.zeros(shape=(len(PotentialList), len(r)))

#	for i in range(0, len(r)):
#		for j in range(0, len(PotentialList)):
#			PotentialValues[j][i] = beta*PotentialList[j](r[i])

#	for i in range(0, len(PotentialList)):
#		pylab.plot(alpha*r, PotentialValues[i][:])

#	pylab.plot(alpha*intersectionRightList, -beta*Energy_Affinity_2(N)*numpy.ones(shape=numpy.shape(intersectionRightList)), 'x')
#	pylab.plot(alpha*intersectionLeftList, -beta*Energy_Affinity_2(N)*numpy.ones(shape=numpy.shape(intersectionLeftList)), 'x')
#	pylab.plot(alpha*numpy.array([r[0], r[-1]]), -beta*Energy_Affinity_2(N)*numpy.ones(shape=(2, 1)))
#	pylab.xlabel('r [Å]')
#	pylab.ylabel('V(r) [eV]')
#	pylab.savefig('testPlot' + str(int(N)))
#	print('intersectionLeftList: ' + str(alpha*intersectionLeftList))
#	print('intersectionRightList: ' + str(alpha*intersectionRightList))
