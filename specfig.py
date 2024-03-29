"""
Spectral binning
"""

import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([20.4, 22.0, 24.4, 27.6, 30.8, 34.0, 38.8, 45.2, 51.6, 58.0, \
        67.6, 80.4, 93.2, 106.0, 125.2, 150.8, 176.4, 202.0, 240.4, 291.6, \
        342.8, 394.0, 470.8, 573.2, 675.6, 778.0, 931.6, 1136.4, 1341.2, 1546.0, \
        1853.2, 2262.8, 2672.4, 3082.0, 3696.4, 4515.6, 5334.8], dtype='float')

#------------------------------------------------------------------------------
# spectrum

Ni = len(x1)

ee = - 2.0

y1 = 4.e7 * np.power(x1,ee)

#------------------------------------------------------------------------------
# Rebin ions
# assume the L2 ion bin number is odd, and keep the last bin intact

Mi = int((Ni-1)/2) + 1
print(f"Mi = {Mi}")

x2 = np.zeros(Mi)
y2 = np.zeros(Mi)
e1 = np.sqrt(x1[0]**3/x1[1])
e2 = np.sqrt(x1[1]*x1[2])
x2[0] = np.sqrt(e1*e2)
y2[0] = y1[0]+y1[1]

idx = 1
for i in np.arange(2,Ni-2,2):
        mm = x1[i-1]*x1[i]*x1[i+1]*x1[i+2]
        x2[idx] = np.power(mm, 0.25)
        y2[idx] = y1[i] + y1[i+1]
        idx += 1

x2[-1] = x1[-1]
y2[-1] = y1[-1]

for i in np.arange(Mi):
    print(f"{x2[i]} {y2[i]}")

logx2 = np.log2(x2)
d2 = logx2[1:] - logx2[0:-1]

logx1 = np.log2(x1)
d1 = logx1[1:] - logx1[0:-1]

for d in d2:
    print(f"diff = {d}")

#------------------------------------------------------------------------------

y1min = y1 - np.sqrt(y1)
y1max = y1 + np.sqrt(y1)

y2min = y2 - np.sqrt(y2)
y2max = y2 + np.sqrt(y2)

#------------------------------------------------------------------------------
# scale factor
fac = 0.5

fig = plt.figure(figsize=(16,6))

ax1 = fig.add_subplot(1, 2, 1)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.plot(x1[:-1], y1[:-1], color ='r')
ax1.plot(x1[:-1], y1[:-1],'o', color = 'r')
ax1.plot(x2[:-1], y2[:-1], color = 'b')
ax1.plot(x2[:-1], y2[:-1],'o', color = 'b')

ax1.set_ylim((0.1,1.e6))
ax1.set_ylabel('Counts')
ax1.set_xlabel('Energy (eV)')

plt.fill_between(x1[:-1],y1min[:-1],y1max[:-1],color='lightsalmon')
plt.fill_between(x2[:-1],y2min[:-1],y2max[:-1],color='lightsteelblue')

yy = [0.1,1.e6]

for i in np.arange(1,Ni-1,2):
        ed = np.sqrt(x1[i]*x1[i+1]) * np.array((1.0,1.0))
        ax1.plot(ed,yy,color='darkgray')

ax2 = fig.add_subplot(1,2,2)
ax2.set_xscale('log')
ax2.plot(x1[1:-1],d1[:-1], color = 'r')
ax2.plot(x1[1:-1],d1[:-1],'o', color = 'r')
ax2.plot(x2[1:-1],d2[:-1], color = 'b')
ax2.plot(x2[1:-1],d2[:-1],'o', color = 'b')

ax2.set_xlim((10,8000))
ax2.plot((1,1.e4),(.5,.5), color='darkgray')

ax2.set_ylabel('log2(bin size)')
ax2.set_xlabel('Energy (eV)')

plt.tight_layout()

plt.show()

