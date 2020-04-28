#python 3 program to plot x^2 and x^3 function on same graph
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize']=5,3
#figure of the size 5in x 3in

x=np.linspace(-1,1,10)
y=x**2
y1=x**3

plt.plot(x,y,'r.',label=r'$y=x^2$')
plt.plot(x,y1,lw=3,color ='g',label =r'$y=x^3$')

plt.axhline(2,color='k') # draw hor axis
plt.axvline(2,color='k') # draw vertical axis

plt.xlim(-1,1)
plt.ylim(-1,1)

plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)

plt.legend(loc=4)
plt.show()
