import numpy
import matplotlib.pyplot
import scipy.integrate

from Metallic_Tomita import *

def WKB_Integral(V, E, Range, epsilon):
    def kappa(r, V, Energy):
        return numpy.sqrt(2*(V(r) - Energy))

    return scipy.integrate.quad(kappa, Range[0], Range[1], args=(V, Energy), full_output = 0, epsabs = epsilon)[0]

Bohr2Angstrom = 0.529177210     # Conversion factor for Bohr -> Ångström
Angstrom2Bohr = 1/Bohr2Angstrom #    - || -  - || -     Ångström -> Bohr
Hartree2eV = 27.211386245       # Conversion factor for Hatree -> eV
eV2Hartree = 1/Hartree2eV       #    - || -  - || -     eV -> Hartree

angularQuantumNumber = 1
shellRadius = 4.5       # Ångström
V_0 = 0.0               # Hartree

WKB_epsilon = 1e-10             # Integration error WKB_Integral
Bisection_epsilon = 1e-10       # Bisection search error

# Create potential of class 'Metallic_Timita'
V = Metallic_Tomita(angularQuantumNumber, V_0, Angstrom2Bohr*shellRadius)

# Create r in range [0.0 80.0] Ångström
r = numpy.linspace(0.0, 80.0, 1e5)

# Plot potential in eV vs Ångström(Fig.6 in article)
fig, ax = matplotlib.pyplot.subplots()
ax.plot(r, Hartree2eV*V(Angstrom2Bohr*r))
ax.set(xlabel='r (Å)', ylabel='U(r) (eV)', title='Fig. 6 Article S. Tomita')
matplotlib.pyplot.xlim(0.0, 90.0)
matplotlib.pyplot.ylim(0.0, 1.6)
matplotlib.pyplot.show()
