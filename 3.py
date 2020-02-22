import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as p3

fig=plt.figure()
ax= p3.Axes3D(fig)

l=7
m=4
n=6

phi=np.linspace (0, 2*np.pi, 100)
t= np.linspace(0, np.pi, 100)

x=np.outer(phi, np.cos(t))+l*np.outer(np.ones(np.size(phi)), np.sin(t))
y=np.outer(phi, np.sin(t))+m*np.outer(np.ones(np.size(phi)), np.sin(t))
z=n*np.outer(np.ones(np.size(phi)), np.sin(t))


ax.plot_surface(x,y,z, color='r')

plt.show()