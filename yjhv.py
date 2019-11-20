import numpy as np
import matplotlib.pyplot as plt
t=np.arange(1,10,0.1)
R=2
x=R*(t-np.sin(t))
y=R*(1-np.cos(t))
plt.plot(x,y,label='dit')
plt.axis('egual')
plt.show
