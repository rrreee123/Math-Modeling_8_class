import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation

sec_y=365*24*60*60
sec_d=24*60*60
years=10
t=np.arange(0,years*sec_y,sec_d*10)

def grav_func(s,t):
    
     (x_a, v_x_a, y_a, v_y_a,
     x_b, v_x_b, y_b, v_y_b, 
     x_c, v_x_c, y_c, v_y_c,
     x_ekz, v_x_ekz,y_ekz, v_y_ekz ) = s
      
     dxdt_a= v_x_a
     dv_xdt_a= (-G*mb* (x_a-x_b)/((x_a-x_b)**2 + (y_a-y_b)**2)**1.5
                -G*mc* (x_a-x_c)/((x_a-x_c)**2 + (y_a-y_c)**2)**1.5)
     dydt_a= v_y_a
     dv_ydt_a=( -G*mb* (y_a-y_b)/((x_a-x_b)**2 + (y_a-y_b)**2)**1.5
                 -G*mc* (y_a-y_c)/((x_a-x_c)**2 + (y_a-y_c)**2)**1.5)
                
     dxdt_b= v_x_b
     dv_xdt_b= (-G*ma* (x_b-x_a)/((x_b-x_a)**2 + (y_b-y_a)**2)**1.5
                -G*mc* (x_b-x_c)/((x_b-x_c)**2 + (y_b-y_c)**2)**1.5)
     dydt_b= v_y_b
     dv_ydt_b= (-G*ma* (y_b-y_a)/((x_b-x_a)**2 + (y_b-y_a)**2)**1.5
                -G*mc* (y_b-y_c)/((x_b-x_c)**2 + (y_b-y_c)**2)**1.5)
     
     dxdt_c= v_x_c
     dv_xdt_c= (-G*ma* (x_c-x_a)/((x_c-x_a)**2 + (y_c-y_a)**2)**1.5
                -G*mb* (x_c-x_b)/((x_c-x_b)**2 + (y_c-y_b)**2)**1.5)
     dydt_c= v_y_c
     dv_ydt_c= (-G*ma* (y_c-y_a)/((x_c-x_a)**2 + (y_c-y_a)**2)**1.5
                -G*mb* (y_c-y_b)/((x_c-x_b)**2 + (y_c-y_b)**2)**1.5)
     
     dxdt_ekz= v_x_ekz
     dv_xdt_ekz= (-G*mc* (x_ekz-x_c)/((x_ekz-x_c)**2 + (y_ekz-y_c)**2)**1.5)
     dydt_ekz= v_y_ekz
     dv_ydt_ekz= (-G*mc* (y_ekz-y_c)/((x_ekz-x_c)**2 + (y_ekz-y_c)**2)**1.5)
    
     return(dxdt_a, dv_xdt_a, dydt_a, dv_ydt_a,
            dxdt_b, dv_xdt_b, dydt_b, dv_ydt_b,
            dxdt_c, dv_xdt_c, dydt_c, dv_ydt_c,
            dxdt_ekz, dv_xdt_ekz, dydt_ekz, dv_ydt_ekz)
     
sun_mass=1.98847*10**30
ma=1.06*sun_mass
mb=0.6*sun_mass
mc=0.3*sun_mass
mekz=10**5

G=6.67*10**(-11)

ae=149.6*10**9

xa0=0
v_xa0=0
ya0=0
v_ya0=1.5*10**4

xb0= 2*ae
v_xb0=0
yb0=0
v_yb0=2*10**4

xc0= 12.3*ae
v_xc0=0
yc0=0
v_yc0=10**4

xekz0= 13*ae
v_xekz0=0
yekz0=0
v_yekz0=np.sqrt(G*mc/(xekz0-xc0)) + v_yc0


s0= (xa0, v_xa0, ya0,v_ya0,
     xb0, v_xb0, yb0,v_yb0,
     xc0, v_xc0, yc0,v_yc0,
     xekz0,v_xekz0, yekz0, v_yekz0)  
  
sol=odeint(grav_func, s0, t)

fig=plt.figure()
planets=[]  

for i in range(0, len(t), 1):
    a, = plt.plot(sol[:i,0], sol[:i, 2], 'r-')
    a_line, = plt.plot(sol[i,0], sol[i, 2], 'ro')
    
    b,= plt.plot(sol[:i,4], sol[:i, 6], '-', color= 'maroon' )
    b_line, = plt.plot(sol[i,4], sol[i, 6],'o', color= 'maroon')
    
    c,= plt.plot(sol[:i,8], sol[:i, 10],  '-', color= 'y')
    c_line, = plt.plot(sol[i,8], sol[i, 10], 'o', color='y')
    
    ekz,= plt.plot(sol[:i,12], sol[:i, 14],  '-', color= 'b')
    ekz_line, = plt.plot(sol[i,12], sol[i, 14], 'o', color='b')
    planets.append([a, a_line, b, b_line,c, c_line, ekz, ekz_line ])
ani = ArtistAnimation(fig, planets, interval= 100)
plt.axis('equal')
ani.save('lebed1.gif')