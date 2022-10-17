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

di = logi[1:] - logi[0:-1]

for d in di:
    print(d)

Ni = len(logi)
x = np.arange(Ni)
i = int(Ni/2)
m = di[i]
b = logi[i] - m * i
yy = np.exp(m*x + b)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_yscale('log')
plt.plot(l2_i)
plt.plot(yy)

plt.show()