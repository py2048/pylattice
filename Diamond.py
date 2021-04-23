from matplotlib import pyplot as plt
from matplotlib import rc
from lattice import *

# Set up the crystal structure
lattice = FCC(3.5597)
basis = Basis([('C',[0,0,0]),('C',[0.25,0.25,0.25])],l_const=3.5597)
crystal = lattice + basis

# Plot a simulated XRD with copper radiation
scattering_data = powder_XRD(crystal,1.5405)
angles, values = spectrumify(scattering_data)
plt.plot(angles,values)

# Add some more info to the plot
plt.title(r'Simulated Powder XRD of Diamond, $\lambda = 1.5405$')
plt.xlabel(r'$2\theta$')
plt.ylabel(r'Scattering Intensity per Cubic Angstrom')
plt.show()
