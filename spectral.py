"""
Spectral binning
"""

import numpy as np
import matplotlib.pyplot as plt

l2_i = np.array([20.4, 22.0, 24.4, 27.6, 30.8, 34.0, 38.8, 45.2, 51.6, 58.0, \
        67.6, 80.4, 93.2, 106.0, 125.2, 150.8, 176.4, 202.0, 240.4, 291.6, \
        342.8, 394.0, 470.8, 573.2, 675.6, 778.0, 931.6, 1136.4, 1341.2, 1546.0, \
        1853.2, 2262.8, 2672.4, 3082.0, 3696.4, 4515.6, 5334.8], dtype='float')

l2_e = np.array([20.4, 22.0, 24.4, 27.6, 30.8, 34.0, 38.8, 45.2, 51.6, 58.0, 67.6, \
        80.4, 93.2, 106.0, 125.2, 150.8, 176.4, 202.0, 240.4, 291.6, 342.8])

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
# Rebin ions

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
        mm = l2_i[i-1]*l2_i[i]*l2_i[i+1]*l2_i[i+2]
        mcheck = np.power(mm, 0.25)
        print(f"{idx} {e1} {l3_i[idx]} {mcheck} {e2}")
        idx += 1

l3_i[-1] = l2_i[-1]

for e in l3_i:
        print(e)
#------------------------------------------------------------------------------
# Rebin electrons

# assume the L2 ion bin number is odd, and keep the last bin intact

Me = int((Ne-1)/2) + 1
print(f"Me = {Me}")

l3_e = np.zeros(Me)
e1 = np.sqrt(l2_e[0]**3/l2_e[1])
e2 = np.sqrt(l2_e[1]*l2_e[2])
l3_e[0] = np.sqrt(e1*e2)

idx = 1
for i in np.arange(2,Ne-2,2):
        e1 = np.sqrt(l2_e[i-1]*l2_e[i])
        e2 = np.sqrt(l2_e[i+1]*l2_e[i+2])
        l3_e[idx] = np.sqrt(e1*e2)
        print(f"{idx} {i} {e1} {l3_e[idx]} {e2}")
        idx += 1

l3_e[-1] = l2_e[-1]

print(80*'-')
for e in l3_e:
        print(e)

#------------------------------------------------------------------------------
# p = L3 bins

plogi = np.log(l3_i)
pdi = plogi[1:] - plogi[0:-1]

ploge = np.log(l3_e)
pde = ploge[1:] - ploge[0:-1]

#------------------------------------------------------------------------------
# constant log bins for comparison

px = np.arange(Mi)
i = int(.7*Mi)
m = pdi[i]
b = plogi[i] - m * i
py = np.exp(m*px + b)

#------------------------------------------------------------------------------

ions = False

fig = plt.figure(figsize=(16,8))

if ions:

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

else:

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_yscale('log')
    ax1.plot(l2_e)
    ax1.plot(l2_e, 'o')

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(de)
    ax2.plot(de, 'o')

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.set_yscale('log')
    ax3.plot(l3_e)
    ax3.plot(l3_e, 'o')

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(pde)
    ax4.plot(pde, 'o')


plt.show()