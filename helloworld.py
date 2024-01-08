
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

plt.figure()
plt.scatter(b_y_array, M_ass_array, c=ageparent_array, cmap='plasma', s=1)
plt.colorbar()
plt.gca().invert_yaxis()
plt.show()


import sys
sys.exit()