
import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as p3

fig=plt.figure()
ax= p3.Axes3D(fig)

phi=np.linspace (0, 0.2*np.pi, 100)
t= np.linspace(0, 2*np.pi, 100)

x=np.outer(phi, np.cos(t))
y=np.outer(phi, np.sin(t))
z=np.outer(phi**2, np.ones(np.size(t)))

ax.plot_surface(x,y,z,color='r')

plt.show()