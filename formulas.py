import math 





def dif_for_slit(L,b):
    x = [[],[]] 
    lmbd = 632.8 #Hм
    P = 3.1416
    if L == 0 or b == 0:
        return 0
    L=float(L)
    b=float(b)
    L*=1000000 #м->мкм
    for m in range(1,24):#m*2
        x[0].append(m*lmbd/b)
        x[0].append(((((m+1)*lmbd/b)-(m*lmbd/b))/2)+m*lmbd/b)#x
        
        #sinus = math.sin((P*b)/lmbd)#Гундырева 
        sinus = math.sin(P*((m+1)+0.5))
        #print(sinus)
        delenie = P*(m+1)+0.5
        #delenie = (P*b)/lmbd #Гундырева 
        #print(delenie)
        x[1].append(pow(sinus/delenie,2))
        x[1].append(0)
    return x

def dif_for_grid(L,b,N):
    x = [[],[]] 
    lmbd = 632.8 #Hм
    P = 3.1416
    if L == 0 or b == 0:
        return 0
    L=float(L)
    b=float(b)
    N=float(N)
    L*=1000000 #м->мкм
    for m in range(0,100):#m*2
        x[0].append(m*lmbd/b)
        x[0].append(((((m+1)*lmbd/b)-(m*lmbd/b))/2)+m*lmbd/b)
        sinus = math.sin(P*N*(m+0.5))
        #print(sinus)
        
        delenie = P*(m+1)+0.5
        
        x[1].append(pow(sinus/delenie,2))
        x[1].append(0)
    #print(size(x[1]))
    #print(size(x[0]))
    return x
#dif_for_slit(1,2)


