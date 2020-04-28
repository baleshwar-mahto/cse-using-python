# plotting 3D axes using python3
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()
ax=plt.axes(projections='3d')

zline=np.linspace(0,15,1000)
xline=np.sin(zline)
yline=np.cos(zline)
ax.plot3D(xline,yline,zline,'gray')

zdata =15*np.random.random(100)
xdata =np.sin(zdata)+0.1*np.random.random(100)
ydata=np.cos(zdata) +0.1*np.random.random(100)
ax.scatter3D(xdata,ydata,zdata,c=zdata,cmap='Greens')
