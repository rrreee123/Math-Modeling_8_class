import matplotlib.pyplot as plt
import numpy as np
def nyb(R=1,a=2,b=3,title='nyb'):
    x=np.arange(-2,2,0.1)
    y=np.arange(-2,2,0.1)
    X,Y=np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[R])
    fxy2=X**2/a**2+Y**2/b**2
    plt.contour(X,Y,fxy,levels=[1])
    plt.show()
    
nyb(0.1)