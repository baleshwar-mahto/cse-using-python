# density plot ,f(x,y)=x^2+y^2
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize']=5,5

x=np.linspace(-1,1,100)
y=np.linspace(-1,1,100)
xv,yv=np.meshgrid(x,y)
z=(xv**2+yv**2)/2
plt.imshow(z,vmin=abs(z).min(),vmax=abs(z).max(),extent=[-1,1,-1,1])

plt.colorbar()
plt.xlabel('$x$',size=20)
plt.ylabel('$y$',size=20)
plt.axes().set_aspect('equal')

plt.tight_layout()
plt.show()


