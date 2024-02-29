import sys
import numpy as np
import matplotlib.pyplot as plt

#initializing
M_ass=[]
b_y=[]
ageparent=[]
metallicity=[]
m_ini=[]
filename=sys.argv[1]

#reading from file
with open(filename, 'r') as file:
    header = file.readline()
    for line in file:
      lines=line.strip()
      columns=lines.split()

      metallicity.append(float(columns[0]))
      m_ini.append(float(columns[1]))
      M_ass.append(float(columns[4]))
      b_y.append(float(columns[8]))
      ageparent.append(float(columns[12]))

#converting to numpy arrays
metallicity_array=np.array(metallicity)
m_ini_array=np.array(m_ini)
M_ass_array=np.array(M_ass)
b_y_array=np.array(b_y)
ageparent_array=np.array(ageparent)

#plotting HR diagram
bins=np.arange(min(ageparent_array), max(ageparent_array) + 0.5, 0.5)
colors=np.digitize(ageparent_array, bins)
plt.figure(1, figsize=(15,10))

for i, edge in enumerate(bins[:-1]):
    plt.scatter(b_y_array[colors == i], M_ass_array[colors == i], label=f'{edge:.1f} <= Gyr < {bins[i+1]:.1f}')  

plt.legend(loc="upper right", fontsize="xx-small")
plt.gca().invert_yaxis()
plt.title('HR diagram')
plt.xlabel('b-y')
plt.ylabel('M abs')
plt.savefig("HR diagram.png")


#binning metallicity for age
metallicity_lt_1 = metallicity_array[ageparent_array < 1]
m_ini_lt_1 = m_ini_array[ageparent_array < 1]

metallicity_1t5 = metallicity_array[(ageparent_array > 1) & (ageparent_array < 5)]
m_ini_1t5 = m_ini_array[(ageparent_array > 1) & (ageparent_array < 5)]

metallicity_gt_5 = metallicity_array[ageparent_array > 5]
m_ini_gt_5 = m_ini_array[ageparent_array > 5]

#plotting metallicity histogram
plt.figure(2)
plt.hist(metallicity_lt_1, bins=np.arange(min(metallicity_lt_1), max(metallicity_lt_1) + 0.1, 0.1).tolist(), alpha=0.5, label='age < 1')
plt.hist(metallicity_1t5, bins=np.arange(min(metallicity_1t5), max(metallicity_1t5) + 0.1, 0.1).tolist(), alpha=0.5, label='1 < age < 5')
plt.hist(metallicity_gt_5, bins=np.arange(min(metallicity_gt_5), max(metallicity_gt_5) + 0.1, 0.1).tolist(), alpha=0.5, label='age > 5')

#computing average and median
average_lt_1 = (float(np.mean(metallicity_lt_1)),float(np.median(metallicity_lt_1)))
average_1t5 = (float(np.mean(metallicity_1t5)),float(np.median(metallicity_1t5)))
average_gt_5 = (float(np.mean(metallicity_gt_5)),float(np.median(metallicity_gt_5)))

#plotting average and median
plt.axvline(x=average_lt_1[0], color='b', linestyle='-', label='avg age < 1')
plt.axvline(x=average_1t5[0], color='r', linestyle='-', label='avg 1 < age < 5')
plt.axvline(x=average_gt_5[0], color='g', linestyle='-', label='avg age > 5')

plt.axvline(x=average_lt_1[1], color='b', linestyle=':', label='med age < 1')
plt.axvline(x=average_1t5[1], color='r', linestyle=':', label='med 1 < age < 5')
plt.axvline(x=average_gt_5[1], color='g', linestyle=':', label='med age > 5')

plt.legend()
plt.title('Metallicity histogram')
plt.xlabel('Metallicity')
plt.ylabel('Number of stars')
plt.savefig("metallicity.png")

#plotting m_ini vs metallicity
fig3, (ax1,ax2,ax3) = plt.subplots(3, 1)
ax1.scatter(m_ini_lt_1, metallicity_lt_1)
ax2.scatter(m_ini_1t5, metallicity_1t5)
ax3.scatter(m_ini_gt_5, metallicity_gt_5)

ax1.title.set_text('Younger than 1Gyr')
ax1.set_xlabel('m_ini')
ax1.set_ylabel('Metallicity')

ax2.title.set_text('1<age<5Gyr')
ax2.set_xlabel('m_ini')
ax2.set_ylabel('Metallicity')

ax3.title.set_text('Older than 5Gyr')
ax3.set_xlabel('m_ini')
ax3.set_ylabel('Metallicity')
plt.savefig("m_ini vs metallicity.png")

plt.show()
