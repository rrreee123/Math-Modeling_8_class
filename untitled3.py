import matplotlib.pyplot as plt
import numpy as np
def parabollagiperbola(a=1,b=1,c=0,title='ParabolaGiperbola'):
    x=np.arange(0.01,10,0.01)
    y1=a*x**2+b*x+c
    y2=a/x
    plt.plot(x,y1,y2,label='my parabola,Giperbola')
    plt.title(title)1)
    plt.legend()
    plt.show()
parabollagiperbola()