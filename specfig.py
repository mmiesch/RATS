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

N1 = len(x1)

ee = - 2.0

y1 = np.power(x1,ee)

#------------------------------------------------------------------------------
# Rebin ions
# assume the L2 ion bin number is odd, and keep the last bin intact

Mi = int((N1-1)/2) + 1
print(f"Mi = {Mi}")

x2 = np.zeros(Mi)
y2 = np.zeros(Mi)
e1 = np.sqrt(x1[0]**3/x2[1])
e2 = np.sqrt(x1[1]*x2[2])
x2[0] = np.sqrt(e1*e2)
y2[0] = y1[0]+y1[1]

idx = 1
for i in np.arange(2,N1-2,2):
        mm = x1[i-1]*x1[i]*x1[i+1]*x1[i+2]
        x2[idx] = np.power(mm, 0.25)
        y2[idx] = y1[i] + y1[i+1]
        idx += 1

y2[-1] = y1[-1]

#------------------------------------------------------------------------------

fig = plt.figure(figsize=(16,8))

ax1 = fig.add_subplot(2, 1, 1)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.plot(x1,y1)
ax1.plot(x2, y2, 'o')

#ax2 = fig.add_subplot(2, 2, 2)
#ax2.plot(di)
#ax2.plot(di, 'o')

plt.show()