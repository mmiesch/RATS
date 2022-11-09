"""
Create a figure for the poster on spectral binning
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
# epam edges

epami = np.array([47,68,115,195,310,580,1060,1900,4800],dtype='float')

epame = np.array([45,62,102,175,315],dtype='float')


#------------------------------------------------------------------------------
# L2 midpoints

l2i = np.array([20.4, 22.0, 24.4, 27.6, 30.8, 34.0, 38.8, 45.2, 51.6, 58.0, \
        67.6, 80.4, 93.2, 106.0, 125.2, 150.8, 176.4, 202.0, 240.4, 291.6, \
        342.8, 394.0, 470.8, 573.2, 675.6, 778.0, 931.6, 1136.4, 1341.2, 1546.0, \
        1853.2, 2262.8, 2672.4, 3082.0, 3696.4, 4515.6, 5334.8], dtype='float')

l2e = np.array([20.4, 22.0, 24.4, 27.6, 30.8, 34.0, 38.8, 45.2, 51.6, 58.0, 67.6, \
        80.4, 93.2, 106.0, 125.2, 150.8, 176.4, 202.0, 240.4, 291.6, 342.8])

#------------------------------------------------------------------------------
# L3 edges

print(f"L2 lengths {len(l2i)} {len(l2e)}")

l3i = []
for i in np.arange(2,len(l2i),2):
        ed = np.sqrt(l2i[i]*l2i[i-1])
        l3i.append(ed)
        print(ed)

print(80*'-')

l3e = []
for i in np.arange(2,len(l2e),2):
        ed = np.sqrt(l2e[i]*l2e[i-1])
        l3e.append(ed)
        print(ed)

l3i = np.array(l3i)
l3e = np.array(l3e)

#------------------------------------------------------------------------------

fig = plt.figure(figsize=(30,8))

# spectrum

sns.set(style='white')
mycmap = sns.color_palette('pastel')
sns.set_palette(mycmap)

x1 = l3i[0]**2/l3i[1]
x2 = l3i[-1]**2/l3i[-2]

xrange = (x1,x2)

ax = fig.add_subplot(2,1,1)
plt.plot(xrange,(1.0,1.0),color='black',linewidth=4)

plt.xticks(fontsize=32)

ax.set_title("Ion Energy Binning",fontsize=40)

ax.set_xlim(xrange)
ax.set_xscale('log')
ax.set_xticks([25,100,1000,6000])
ax.set_xticklabels(['25 keV/n','100 keV/n','1 MeV/n','6 MeV/n'])

ax.set_ylim((0,2))
ax.set(ylabel=None)
ax.set_yticklabels([''])

plt.fill_between((x1,epami[0]),(1,1),(2,2))
for i in np.arange(1,len(epami)):
    plt.fill_between((epami[i-1],epami[i]),(1,1),(2,2))
plt.fill_between((epami[-1],x2),(1,1),(2,2))

plt.fill_between((x1,l3i[0]),(0,0),(1,1))
for i in np.arange(1,len(l3i)):
    plt.fill_between((l3i[i-1],l3i[i]),(0,0),(1,1))
plt.fill_between((l3i[-1],x2),(0,0),(1,1))


yy = np.array((1,2))
xx = np.array((1.0,1.0))
for e in epami:
   plt.plot(e*xx,yy,color='black',linewidth=4)

yy = np.array((0,1))
for e in l3i:
   plt.plot(e*xx,yy,color='black',linewidth=4)

#---------------------------------------------------------------------

x1 = l3e[0]**2/l3e[1]
x2 = l3e[-1]**2/l3e[-2]

xrange = (x1,x2)

ax2 = fig.add_subplot(2,1,2)
plt.plot(xrange,(1.0,1.0),color='black',linewidth=4)

plt.xticks(fontsize=32)

ax2.set_title("Electron Energy Binning",fontsize=40)

ax2.set_xlim(xrange)
ax2.set_xscale('log')
ax2.set_xticks([25,100,300])
ax2.set_xticklabels(['25 keV','100 keV','300 keV'])

ax2.set_ylim((0,2))
ax2.set(ylabel=None)
ax2.set_yticklabels([''])

plt.fill_between((x1,epame[0]),(1,1),(2,2))
for i in np.arange(1,len(epame)):
    plt.fill_between((epame[i-1],epame[i]),(1,1),(2,2))
plt.fill_between((epame[-1],x2),(1,1),(2,2))

plt.fill_between((x1,l3e[0]),(0,0),(1,1))
for i in np.arange(1,len(l3e)):
    plt.fill_between((l3e[i-1],l3e[i]),(0,0),(1,1))
plt.fill_between((l3e[-1],x2),(0,0),(1,1))

yy = np.array((1,2))
xx = np.array((1.0,1.0))
for e in epame:
   plt.plot(e*xx,yy,color='black',linewidth=4)

yy = np.array((0,1))
for e in l3e:
   plt.plot(e*xx,yy,color='black',linewidth=4)

#---------------------------------------------------------------------

plt.tight_layout()

plt.show()
