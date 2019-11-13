def  git(m_ast,v_stolk):
    c=4200
    m=1.4*10**21
    t1=15
    
    k=(m_ast*v_stolk**2)/2
    t2=k/c/m+t1
    t3=t2-t1
    print(t3)
    if t3>50 and t3<100:
        print('все сдохнут')
    if t3>30 and t3<50:
        print('сдохнит половина')
 