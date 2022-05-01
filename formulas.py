import math 
import cmath
from pickletools import long1




def dif_for_slit(L,b):
    x = [[],[]] 
    lmbd = 632.8 #Hм
    P = 3.1416
    if L == 0 or b == 0:
        return 0
    L=float(L)
    b=float(b)
    L*=1000000000
    for m in range(0,10):#m*2
        x[0].append((L*lmbd*m)/b)# минимумы
        x[0].append(abs(2*m+1)*(lmbd/2))#максимумы
        sinus = math.sin((m+1)*(P*b*(x[0][2*m+1]/pow((pow(x[0][m*2+1],2)+pow(L,2)),0.5))/lmbd))
        #print(sinus)
        delenie = math.sin((P*b*(abs(x[0][m*2+1])/pow((pow(abs(x[0][m*2+1]),2)+pow(L,2)),0.5)))/lmbd )#
        #print(delenie)
        print("")
        #x[1].append(math.sin((P*b*abs(2*m+1)*(lmbd/2)/lmbd)/(lmbd*L*2))/((P*2*b*abs(2*m+1)*(lmbd/2))/(lmbd*L*2))/(lmbd*L*2)) # значение при максимумах
       
        x[1].append(pow(sinus/delenie,2))
    print(x[1])
    print(x[0])
    return x


dif_for_slit(1,2)


