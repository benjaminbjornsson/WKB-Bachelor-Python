import numpy
import matplotlib.pyplot
import scipy.integrate
import scipy.special

from heat_capacity import *

from Metallic import *

def WKB_Integral(V, E, Range, epsilon):
    def kappa(r, V, Energy):
        return numpy.sqrt(2*(V(r) - Energy))

    return 2*scipy.integrate.quad(kappa, Range[0], Range[1], args=(V, Energy), full_output = 0, epsabs = epsilon)[0]


Bohr2Angstrom = 0.529           # Conversion factor for Bohr -> Angstrom
Angstrom2Bohr = 1/Bohr2Angstrom #    - || -  - || -      Angstrom -> Bohr
Hartree2eV = 27.211386245988    # Conversion factor for Hatree -> eV
eV2Hartree = 1/Hartree2eV       #    - || -  - || -     eV -> Hartree

angularQuantumNumber = 1
shellRadius = 4.5       # Ångström
V_0 = 0.0               # Hartree

WKB_epsilon = 1e-10             # Integration error WKB_Integral
Bisection_epsilon = 1e-10       # Bisection search error

# Create potential of class 'Metallic'
V = Metallic(angularQuantumNumber, V_0, Angstrom2Bohr*shellRadius)

# Create r in range [0.0 80.0] Ångström
r = numpy.linspace(0.0, 80.0, int(1e5))

# Plot potential in eV vs Ångström(Fig.6 in article)
#fig, ax = matplotlib.pyplot.subplots()
#ax.plot(r, Hartree2eV*V(Angstrom2Bohr*r))
#ax.set(xlabel='r (Å)', ylabel='U(r) (eV)', title='Fig. 6 Article S. Tomita')
#matplotlib.pyplot.xlim(0.0, 90.0)
#matplotlib.pyplot.ylim(0.0, 1.6)
#matplotlib.pyplot.show()

# Plot expected_energy and heat_capacity
#temperature = numpy.linspace(7.5, 2000, int(1e5))
#fig, (ax1, ax2) = matplotlib.pyplot.subplots(1,2)

#ax1.plot(temperature, expected_energy_vectorized(temperature))
#ax1.plot(temperature[temperature > 500], linear_energy(temperature[temperature > 500]))
#ax2.plot(temperature, heat_capacity_vectorized(temperature))

#matplotlib.pyplot.show()

# Plot populations and rate(Fig 8. in article)
k_B = 8.617333262145e-5                                         # eV/K
A_0 = 7.0e8                                                     # s-1
epsilon = numpy.array([0.4, 0.200, 0.222, 0.305, 0.335])        # eV
print('epsilon: ', epsilon)
degeneracy_C60 = numpy.array([0, 1, 5, 9, 9])

print('degeneracy_C60: ', degeneracy_C60)

rates = numpy.array([0, 0.05, 0.70, 800, 5000])



def k_0(temperature):
    return A_0*numpy.exp(-epsilon[0]/k_B*numpy.divide(1, temperature))

def k_1(probabilities):
    for i in range(1, 5):
        probabilities[i, :] = rates[i]*probabilities[i, :]
    return numpy.sum(probabilities, axis = 0)

def probability(temperature, i):
#    return (temperature - (epsilon[i] - epsilon[1])/(heat_capacity(temperature)))
    return degeneracy_C60[i]*numpy.exp(-(epsilon[i] - epsilon[1])/(k_B*(temperature - (epsilon[i] - epsilon[1])/(2*heat_capacity(temperature)))))

probability_vectorized = numpy.vectorize(probability)

temperature = numpy.linspace(108.0, 500.0, int(1e3))

probabilities = numpy.zeros(shape = temperature.shape)

for i in range(1,5):
    probabilities = numpy.vstack((probabilities, probability_vectorized(temperature, i)))

for i in range(probabilities.shape[1]):
    probabilities[:, i] = probabilities[:, i]/numpy.sum(probabilities[:, i])

fig, (ax1, ax2) = matplotlib.pyplot.subplots(2,1)

for i in range(1, 5):
    ax1.plot(temperature, probabilities[i][:])

ax1.set_xlim(100.0, 500)
ax1.set_ylim(0.0, 1.0)

ax1.yaxis.set_ticks_position('both')

ax2.semilogy(temperature, k_0(temperature))
ax2.semilogy(temperature, k_1(probabilities))

ax2.set_xlim(100, 500)
ax2.set_ylim(1e-1, 1e5)

ax2.yaxis.set_ticks_position('both')

matplotlib.pyplot.show()
