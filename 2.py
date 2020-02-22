
import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as p3

fig=plt.figure()
ax= p3.Axes3D(fig)

h=7

phi=np.linspace (0, 2*np.pi, 100)
t= np.linspace(0, 2*np.pi, 100)

x=np.outer(phi, np.cos(t))
y=np.outer(phi, np.sin(t))
z=h*np.outer(np.ones(np.size(phi)), t)


ax.plot_surface(x,y,z, color='y')

plt.show()