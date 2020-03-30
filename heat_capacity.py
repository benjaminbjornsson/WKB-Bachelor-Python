import numpy
import matplotlib.pyplot

Hartree2eV = 27.211386245988    # Conversion factor for Hatree -> eV
eV2Hartree = 1/Hartree2eV       #    - || -  - || -     eV -> Hartree

cm2eV = (1.23984193*1e-4)
k_B = 8.617333262145e-5         # eV/K
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
nu.sort()
#nu = numpy.where(nu > 1100, 0.9*nu, nu)
nu = 0.9*nu

%nu = numpy.array([272, 343, 353, 403, 433,
%                485, 496, 526, 534, 553,
%                567, 568, 575, 668, 709,
%                736, 743, 753, 756, 764,
%                772, 776, 796, 831, 961,
%                973, 984, 1079, 1099, 1182,
%                1205, 1223, 1252, 1289, 1309,
%                1310, 1344, 1345, 1422, 1425,
%                1429, 1470, 1482, 1525, 1567, 1575])

nu.sort()

degeneracy = numpy.array([5, 3, 4, 5,
                5, 4, 1, 3, 5, 3, 4, 3,
                3, 5, 5, 4, 5, 3, 3, 4,
                5, 4, 3, 3, 4, 3, 1, 4,
                5, 3, 3, 5, 5, 3, 4, 4,
                5, 3, 4, 5, 3, 1, 4, 3,
                5, 5])

energy = cm2eV*nu # eV

def expected_energy(temperature):
    exponential_factors = numpy.exp(energy/(k_B*temperature))
    return numpy.sum(numpy.multiply(degeneracy, numpy.divide(energy, exponential_factors - 1.0)))

def heat_capacity(temperature):
    exponential_factors = numpy.exp(energy/(k_B*temperature))
    return 1/(k_B*temperature**2)*numpy.sum(numpy.multiply(numpy.multiply(degeneracy, exponential_factors), numpy.divide(numpy.square(energy), numpy.square(exponential_factors - 1.0))))

expected_energy_vectorized = numpy.vectorize(expected_energy)
heat_capacity_vectorized = numpy.vectorize(heat_capacity)

linear_energy = lambda T: 7.4 + 0.0138*(T - 1000)
