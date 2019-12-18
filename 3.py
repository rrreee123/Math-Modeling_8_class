import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,100, 1)
def number_func(v,t):
    dndt= (F - y*v**2)/m
    return dndt   
v_0 = 0
y = 0.1
m = 1
F = 5

solve = odeint(number_func,v_0,t)
plt.plot(t,solve[:,0])
plt.show()
