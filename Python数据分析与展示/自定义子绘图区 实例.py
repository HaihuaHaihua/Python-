#尝试失败
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

plt.subplot2grid((3,3),(0,0))
gs1 = gridspec.GridSpec(3,3)
a1 = plt.subplot(gs1[0,0])
aa1 = np.arange(0.0,5.0,0.02)
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

a2 = plt.subplot(gs1[0,1])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

a3 = plt.subplot(gs1[0,2])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

a4 = plt.subplot(gs1[1,0])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

a5 = plt.subplot(gs1[1,1])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

a6 = plt.subplot(gs1[1,2])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

a7 = plt.subplot(gs1[2,0])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

a8 = plt.subplot(gs1[2,1])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

a9 = plt.subplot(gs1[2,2])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')
##
plt.subplot2grid((3,3),(0,1))
gs2 = gridspec.GridSpec(3,3)
b1 = plt.subplot(gs1[0,0])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

b2 = plt.subplot(gs1[0,1])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

b3 = plt.subplot(gs1[0,2])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

b4 = plt.subplot(gs1[1,0])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

b5 = plt.subplot(gs1[1,1])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

b6 = plt.subplot(gs1[1,2])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

b7 = plt.subplot(gs1[2,0])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

b8 = plt.subplot(gs1[2,1])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

b9 = plt.subplot(gs1[2,2])
plt.plot(aa1,np.cos(2*np.pi*aa1),color='blue')

plt.grid(True)
plt.show()

