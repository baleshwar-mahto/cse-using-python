#plottting 3D vector using python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

plt.gca(projection='3d') #gca = get current axis

# vector plot
x= np.linspace(-10,10,5)
y= np.linspace(-10,10,5)
z= np.linspace(-10,10,5)

xv,yv,zv =np.meshgrid(x,y,z)
#meshgrid is a 3D grid :(xv,yv,zv)=coordinate

plt.quiver(xv,yv,zv,-xv,-yv,-zv)
plt.show()
