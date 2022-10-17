"""
Spectral binning
"""

import numpy as np
import matplotlib.pyplot as plt

l2_i = np.array([20.4, 22.0, 24.4, 27.6, 30.8, 34.0, 38.8, 45.2, 51.6, 58.0, \
        67.6, 80.4, 93.2, 106.0, 125.2, 150.8, 176.4, 202.0, 240.4, 291.6, \
        342.8, 394.0, 470.8, 573.2, 675.6, 778.0, 931.6, 1136.4, 1341.2, 1546.0, \
        1853.2, 2262.8, 2672.4, 3082.0, 3696.4, 4515.6, 5334.8], dtype='float')

l2_e = np.array([20.4, 22.0, 27.6, 30.8, 34.0, 38.8, 45.2, 51.6, 58.0, 67.6, 80.4, \
        93.2, 106.0, 125.2, 150.8, 176.4, 202.0, 240.4, 291.6, 342.8])

logi = np.log(l2_i)
loge = np.log(l2_e)

#------------------------------------------------------------------------------
Ni = len(logi)
Ne = len(loge)

# log bin size
di = logi[1:] - logi[0:-1]
de = loge[1:] - loge[0:-1]

#------------------------------------------------------------------------------
# constant log bins for comparison

x = np.arange(Ni)
i = int(0.7*Ni)
m = di[i]
b = logi[i] - m * i
yy = np.exp(m*x + b)

#------------------------------------------------------------------------------
# Now rebin

# assume the L2 ion bin number is odd, and keep the last bin intact

Mi = int((Ni-1)/2) + 1
print(f"Mi = {Mi}")

l3_i = np.zeros(Mi)
e1 = np.sqrt(l2_i[0]**3/l2_i[1])
e2 = np.sqrt(l2_i[1]*l2_i[2])
l3_i[0] = np.sqrt(e1*e2)

idx = 1
for i in np.arange(2,Ni-2,2):
        e1 = np.sqrt(l2_i[i-1]*l2_i[i])
        e2 = np.sqrt(l2_i[i+1]*l2_i[i+2])
        l3_i[idx] = np.sqrt(e1*e2)
        #print(f"{idx} {e1} {l3_i[idx]} {e2}")
        idx += 1

l3_i[-1] = l2_i[-1]

for e in l3_i:
        print(e)

#------------------------------------------------------------------------------
# p = L3 bins

plogi = np.log(l3_i)
pdi = plogi[1:] - plogi[0:-1]

#------------------------------------------------------------------------------
# constant log bins for comparison

px = np.arange(Mi)
i = int(.7*Mi)
m = pdi[i]
b = plogi[i] - m * i
py = np.exp(m*px + b)

#------------------------------------------------------------------------------

fig = plt.figure(figsize=(16,8))

ax1 = fig.add_subplot(2, 2, 1)
ax1.set_yscale('log')
ax1.plot(l2_i)
ax1.plot(l2_i, 'o')
ax1.plot(yy)

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(di)
ax2.plot(di, 'o')

ax3 = fig.add_subplot(2, 2, 3)
ax3.set_yscale('log')
ax3.plot(l3_i)
ax3.plot(l3_i, 'o')
ax3.plot(py)

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(pdi)
ax4.plot(pdi, 'o')

plt.show()