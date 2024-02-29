
import numpy as np
import matplotlib.pyplot as plt
import sys

metallicity_array = np.loadtxt("Nemo_6670.dat", skiprows=1, usecols=(0,1))

print(metallicity_array)