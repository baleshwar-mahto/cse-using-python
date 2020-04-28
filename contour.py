# contour plot , f(x,y)=-log{(x^2+y^2)}^1/2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from pylab import rcParams
rcParams['figure.figsize'] =5,5

plt.figure()
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)

xv,yv =np.meshgrid(x,y)
z=-np.log(np.sqrt((xv**2+yv**2)))
curves=plt.contour(xv,yv,z,6)
plt.colorbar()

plt.xlabel('$x$',size=20)
plt.ylabel('$y$',size=20)
plt.axes().set_aspect('equal')
plt.tight_layout()
plt.show()
