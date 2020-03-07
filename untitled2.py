import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation

sec_y=365*24*60*60
sec_d=24*60*60
years=10
t=np.arange(0,years*sec_y,sec_d*10)

def grav_func(s,t):
    
     (x_a, v_x_a, y_a, v_y_a ) = s
      
     dxdt_a= v_x_a
     dv_xdt_a= (-G*mb* (x_a)/((x_a)**2 + (y_a)**2)**1.5)
     dydt_a= v_y_a
     dv_ydt_a=( -G*mb* (y_a)/((x_a)**2 + (y_a)**2)**1.5)
                
                
    
     return(dxdt_a, dv_xdt_a, dydt_a, dv_ydt_a)
     
sun_mass=1.98847*10**30
mb=0.6*sun_mass


G=6.67*10**(-11)

ae=149.6*10**9

xa0=0.3288666467385834
v_xa0=-0.944376370237481
ya0=-0.944376370237481
v_ya0=-0.3288666467385834




s0= (xa0, v_xa0, ya0,v_ya0,)  
  
sol=odeint(grav_func, s0, t)

fig=plt.figure()
planets=[]  

for i in range(0, len(t), 1):
    a, = plt.plot(sol[:i,0], sol[:i, 2], 'r-')
    a_line, = plt.plot(sol[i,0], sol[i, 2], 'ro')
    
    
    planets.append([a, a_line ])
ani = ArtistAnimation(fig, planets, interval= 100)
plt.axis('equal')
ani.save('lebed1.gif')