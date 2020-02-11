import numpy
import matplotlib.pyplot
import scipy.integrate
from Dielectric import Dielectric
from Coulombic import Coulombic

gamma = 1e-10
relativeDielectricConstant = 4.4
angularQuantumNumber = range(0, 3)
alpha = 0.529
beta = 27.211
V_0 = 0.0/beta
timeConversionFactor = 2.42*1e-17

R_0 = 3.55/alpha
DeltaR = 1.46/alpha

def shellRadius(N):
    return numpy.sqrt(N)/numpy.sqrt(60)*R_0 + DeltaR


def Energy_Affinity_2(N):
    return (2.8521 - 15.7922/(alpha*shellRadius(N)))/beta

def kappa(r, V, Energy):
    return numpy.sqrt(2*(V(r) - Energy))

def tau(V, Energy, Range):
    f = numpy.exp(scipy.integrate.quad(kappa, Range[0], Range[1], args=(V, Energy), full_output = 0, epsabs=1e-15)[0])
    Tr = 4.0/(2.0*f + 1.0/(2.0*f))**2
#    Tr = 1/(f**2)
    vinc = numpy.sqrt(2.0*Energy)

    if isinstance(V, Dielectric):
        rs = V.getShellRadius() + V.getDelta()
    else:
        rs = V.getShellRadius()
    return (2.0*rs)/(Tr*vinc)

#NList = [20, 40, 60, 64, 68, 70, 74, 78, 82, 84, 86, 88, 90]
NList = [60]

for N in NList:
    if -1/Energy_Affinity_2(N) < 0:
        break
    PotentialList = []
    for l in angularQuantumNumber:
        PotentialList.append(Dielectric(l, V_0, shellRadius(N), relativeDielectricConstant))
        PotentialList.append(Coulombic(l, V_0, shellRadius(N)))
 
#    Energy = 0.333/beta
    Energy = -Energy_Affinity_2(N)
    rangeRight = [shellRadius(N) + 2.0/alpha, 1/Energy + 10.0/alpha]
    rangeLeft = [0.0, shellRadius(N) + 2.0/alpha]

    lifeTimes = []
    for i in range(0, len(PotentialList)):
        l = PotentialList[i].getAngularQuantumNum()
        if isinstance(PotentialList[i], Dielectric):
            leftLimit = PotentialList[i].getIntersect(Energy, rangeLeft, 1, gamma)
        else:
            leftLimit = shellRadius(N)

        rightLimit = PotentialList[i].getIntersect(Energy, rangeRight, -1, gamma)
        Range = numpy.array([leftLimit, rightLimit])
        try:
            RangeList = numpy.vstack([RangeList, Range])
        except:
            RangeList = Range

        lifeTimes.append(format(tau(PotentialList[i], Energy, Range)*timeConversionFactor, '.1e'))

#    print(lifeTimes)
    print(lifeTimes[1:len(lifeTimes):2], lifeTimes[0:len(lifeTimes):2])
    nameList = []
    tau = []
    for i in range(len(RangeList)):
        if isinstance(PotentialList[i], Dielectric):
            continue
        r1 = RangeList[i][0]
        r2 = RangeList[i][1]
        gamma = numpy.sqrt(2*Energy)*(r2*numpy.arccos(numpy.sqrt(r1/r2)) - numpy.sqrt(r1*(r2 - r1)))
        f = numpy.exp(gamma)
        Tr = 1/(f**2)
        velocity = numpy.sqrt(2.0*Energy)
        tau.append(format(timeConversionFactor*(2.0*r1)/(Tr*velocity), '.1e'))
    print(tau)
#    Range = numpy.array([0.0, (1/Energy)/alpha + 10.0])
#    fig = matplotlib.pyplot.figure()
#    print(RangeList)
#    for Potential in PotentialList:
#        numpy.plot()

#    matplotlib.pyplot.plot(alpha*numpy.array([0.0, Range[1]]), beta*Energy*numpy.ones(2))
#    matplotlib.pyplot.ylim(-0.2, 4.0)
#    matplotlib.pyplot.show()
#    matplotlib.pyplot.savefig('testPlot' + str(N))
