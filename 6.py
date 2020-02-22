import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation 

second_in_year=365*24*60*60
second_in_day=24*60*60
years = 1

t = np.arange(0,years*second_in_year,second_in_day)

def move_func(s,t):
    (x1,v_x1,y1,v_y1,
    x2,v_x2,y2,v_y2,
    x3,v_x3,y3,v_y3) = s
    
    dxdt1 =v_x1
    dv_xdt1 = (-G*m2*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
            -G*m3*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5)
    
    dydt1 =v_y1
    dv_ydt1 = (-G*m2*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
            -G*m2*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5)
   
    
    dxdt2 =v_x2
    dv_xdt2 = (-G*m1*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
            -G*m3*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5)
    
    dydt2 =v_y2
    dv_ydt2 = (-G*m1*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
            -G*m3*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5)
    
    
    dxdt3 =v_x3
    dv_xdt3 = (-G*m1*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
            -G*m3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5)
    
    dydt3 =v_y3
    dv_ydt3 = (-G*m1*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5
            -G*m2*(y3-y2)/((x3-x2)**2+(y3-y2)**2)**1.5)
    return(dxdt1,dv_xdt1,dydt1,dv_ydt1,
           dxdt2,dv_xdt2,dydt2,dv_ydt2,
           dxdt3,dv_xdt3,dydt3,dv_ydt3)
    
xA =5.3*149.6*10**9
v_xA = 0
yA = 0
v_yA= 13000

xB = 7*149.6*10**9
v_xB = 0
yB = 0
v_yB =15000

xC =11*149.6*10**9 
v_xC =0 
yC =0
v_yC=11000

s0 =(xA,v_xA,yA,v_yA,
    xB,v_xB,yB,v_yB,
    xC,v_xC,yC,v_yC)

m1 = 1.06*1.98847*10**30

m2 = 0.6*1.98847*10**30

m3 = 0.3*1.98847*10**30

G = 6.67*10**(-11)

sol = odeint(move_func,s0,t)

fig = plt.figure()
bodys = []

for i in range(0, len(t), 1):
    body1, = plt.plot(sol[:i,0],sol[:i,2],'-', color= 'y')
    body1_line, = plt.plot(sol[i,0],sol[i,2],'o', color= 'y')

    body2, = plt.plot(sol[:i,4],sol[:i,6],'-', color= 'g')
    body2_line, = plt.plot(sol[i,4],sol[i,6],'o', color= 'g')

    body3, = plt.plot(sol[:i,8],sol[:i,10],'-', color= 'r')
    body3_line, = plt.plot(sol[i,8],sol[i,10],'o', color= 'r')
    
    bodys.append([body1,body1_line,body2,body2_line,body3,body3_line])

ani = ArtistAnimation(fig,bodys, interval=100)
plt.axis('equal')
ani.save('N_body_G.gif')



