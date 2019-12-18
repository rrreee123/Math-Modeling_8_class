import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,100,0.1)
def baktery(n,t):
    dndt = k*n
    return dndt
k = 0.05
n_0= 1
solve = odeint(baktery,n_0,t)
plt.plot(t,solve[:,0])
plt.show() 