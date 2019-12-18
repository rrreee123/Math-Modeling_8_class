import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,10, 1)
def number_func(n,t):
    dndt= -k*n*t
    return dndt   
n_0 = 1000
k = 0.05
solve = odeint(number_func,n_0,t)
plt.plot(t,solve[:,0])
plt.show()
