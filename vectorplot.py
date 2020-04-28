# plotting a 2-D vector using python 3 // vector r=(-x,-y)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from pylab import rcParams
rcParams['figure.figsize']=5,3

# vector plot
x=np.linspace(-2,2,10)
y=np.linspace(-2,2,10)
xv, yv =np.meshgrid(x,y)
# meshgrid is a 2D grid : (xv,yv) provides the coordinate at points a mesh of Nx*Ny grid

plt.figure()
plt.quiver(xv,yv,-xv,-yv)
#quiver =array:At point (xv,yv), make vector of (-xv**3,-yv**y)
plt.show()
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)

plt.xticks(np.linspace(-2,2,5),endpoint=True)
plt.yticks(np.linspace(-2,2,5), endpoint=True)
plt.axes().set_aspect('equal')
plt.tight_layout()

plt.show()

