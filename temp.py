import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.arange(0.01, 4*np.pi,0.01)
R=1
x = R * np.sin(2*t)
y = R*(1-np.cos(2*t))
z = R*(2*np.cos(t))
ax.plot(x,y,z,label='Dutch')
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D TEST')
plt.show()