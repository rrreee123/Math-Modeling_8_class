import numpy as np
import matplotlib.pyplot as plt
R=15
t=np.arange(1,10,0.1)
x=R*np.cos(t)**3
y=R*np.sin(t)**3
plt.plot(x,y,label='dit')
plt.show


