
import numpy as np
import matplotlib.pyplot as plt

print("hello world")

M_ass=[]
b_y=[]
ageparent=[]
filename="Nemo_6670.dat"

with open(filename, 'r') as file:
    header = file.readline()
    for line in file:
      lines=line.strip()
      columns=lines.split()

      M_ass.append(float(columns[4]))
      b_y.append(float(columns[8]))
      ageparent.append(float(columns[12]))

M_ass_array=np.array(M_ass)
b_y_array=np.array(b_y)
ageparent_array=np.array(ageparent)

#plt.figure()
#plt.scatter(b_y_array, M_ass_array, c=ageparent_array, cmap='plasma', s=1)
#plt.colorbar()
#plt.gca().invert_yaxis()
#plt.show()

metallicity_array = np.loadtxt("Nemo_6670.dat", skiprows=1, usecols=(0,))

metallicity_lt_1 = metallicity_array[ageparent_array < 1]
metallicity_between_1_and_5 = metallicity_array[(ageparent_array > 1) & (ageparent_array < 5)]
metallicity_gt_5 = metallicity_array[ageparent_array > 5]

plt.figure()
plt.hist(metallicity_lt_1, bins=np.arange(min(metallicity_lt_1), max(metallicity_lt_1) + 0.1, 0.1).tolist(), alpha=0.5, label='age < 1')
plt.hist(metallicity_between_1_and_5, bins=np.arange(min(metallicity_between_1_and_5), max(metallicity_between_1_and_5) + 0.1, 0.1).tolist(), alpha=0.5, label='1 < age < 5')
plt.hist(metallicity_gt_5, bins=np.arange(min(metallicity_gt_5), max(metallicity_gt_5) + 0.1, 0.1).tolist(), alpha=0.5, label='age > 5')
plt.legend()
plt.show()


import sys
sys.exit()