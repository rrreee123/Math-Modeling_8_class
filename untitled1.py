import numpy as np
def massiv(a):
    s=1
    for i in range(0 ,len(a), 1):
        s=s*a[i]
        
    print(s)
        
f=np.arange(2,6,2)
massiv(f)
