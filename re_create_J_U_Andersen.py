import numpy
import matplotlib.pyplot

cm2eV = (1.23984193*1e-4)
k_B = 8.617333262145e-5                         # eV/K
nu = numpy.array([610, 1667, 
                627, 865, 1410, 
                591, 784, 919, 1483, 
                491, 579, 856, 1235, 1404, 1650, 
                263, 447, 771, 924, 1261, 1407, 1596, 1722,
                972, 
                577, 719, 1353, 1628, 
                348, 776, 1134, 1314, 1687, 
                362, 750, 914, 1110, 1436, 1587, 
                403, 546, 706, 822, 1344, 1467, 1709])    # cm-1

nu = numpy.where(nu > 900, nu - 170, nu)

degeneracy = numpy.array([1, 2,
                1, 2, 3,
                1*2, 2*2, 2*3, 2*4,
                1, 2, 3, 4, 5, 6,
                1, 2, 3, 4, 5, 6, 7, 8,
                1,
                1, 2, 3, 4,
                1*1, 2*2, 2*3, 2*4, 2*5,
                1, 2, 3, 4, 5, 6,
                1, 2, 3, 4, 5, 6, 7])

print('Num degeneracy = ', numpy.sum(degeneracy))
print('Len nu = ', len(nu))

print(sorted(nu))

energy = cm2eV*nu                                     # eV
temperature = numpy.linspace(5.0, 2000.0, int(1e5))

def expected_energy(temperature):
    exponential_factors = numpy.exp(energy/(k_B*temperature))
    return numpy.sum(numpy.multiply(degeneracy, numpy.divide(energy, exponential_factors - 1.0)))

linear_energy = lambda T: 7.4 + 0.0138*(T - 1000)

expected_energy_vectorized = numpy.vectorize(expected_energy)

fig, ax = matplotlib.pyplot.subplots()

ax.plot(temperature, expected_energy_vectorized(temperature))
ax.plot(temperature[temperature > 500], linear_energy(temperature[temperature > 500]))

matplotlib.pyplot.xlabel('Temperature [K]')
matplotlib.pyplot.ylabel('Energy [eV]')

matplotlib.pyplot.show()

def heat_capacity(temperature):
    boltzmann_factors = numpy.exp(-energy/(k_B*temperature))
    partition_function = numpy.sum(boltzmann_factors)
