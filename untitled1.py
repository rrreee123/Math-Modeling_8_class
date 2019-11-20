import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
fig, ax = plt.subplots()
astroida, = plt.plot([],[],'o')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
x, y = [], []
R=1
def astroida7(t):
    x.append(R*np.cos(t)**3)
    y.append(R*np.sin(t)**3)
    astroida.set_data(x,y)
    
ani=FuncAnimation(fig,
                  astroida7,
                  frames=np.arange(0,2*np.pi,0.1),
                  interval=100)
ani.save('ani.gif')
