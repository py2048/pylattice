from matplotlib import pyplot as plt
from lattice import *

# Set up the crystal structure
lattice = FCC(5.42)
basis = Basis([('Siv',[0,0,0]),('Siv',[0.25,0.25,0.25])],l_const=5.42)
crystal = lattice + basis

# Plot a simulated XRD with copper radiation
scattering_data = powder_XRD(crystal, 1.5405)
angles, values = spectrumify(scattering_data)
plt.plot(angles,values)

# Add some more info to the plot
plt.title(r'Simulated Powder XRD of Silicon, $\lambda = 1.5405$')
plt.xlabel(r'$2\theta$')
plt.ylabel(r'Scattering Intensity per Cubic Angstrom')
plt.show()
