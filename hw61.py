import numpy as np
def Rosenbrock(ap):
    return (1-ap[0])**2+100*(ap[1]-ap[0]**2)**2
def sort():
    global P
    value=[Rosenbrock(P[0]),Rosenbrock(P[1]),Rosenbrock(P[2])]
    tmp=0
    for i in range(0,1):
        for j in range(i+1,2):
            if value[i]>value[j]:
                tmp=P[i]
                P[i]=P[j]
                P[j]=tmp
                tmp=value[i]
                value[i]=value[j]
                value[j]=tmp
def findx0():
    sumx=0
    sumy=0
    global P
    for ap in P:
        sumx=sumx+ap[0]
        sumy=sumy+ap[1]
    return [sumx/2,sumy/2]

def ReflectionExpansionandContraction(x0):
    global a , P , p , r , o
    xr=x0+a*(x0-P[2])
    if Rosenbrock(xr)<Rosenbrock(P[1]):#reflecion
        if Rosenbrock(xr)>=Rosenbrock(P[0]):
            P[2]=xr
            return True
        else :#expection
            xe=x0+r(xr-x0)
            if Rosenbrock(xe)<Rosenbrock(xr):
                P[2]=xe
                return True
            else:
                P[2]=xr
                return True
    else:#contraction
        xc=x0+p*(P[2]-x0)
        if Rosenbrock(xc)<Rosenbrock(P[2]):
            P[2]=xc
            return True
        else :
            return False
def shrink():
    global o,P
    for i in range(1,2):
        P[i]=P[0]+o*(P[i]-P[0])

def sd():
    global P
    SD2=0
    average=0
    for ap in P:
        average=average+Rosenbrock(ap)
    average=average/3
    for ap in P:
        SD2=SD2+(Rosenbrock(ap)-average)**2
    SD= (SD2/3)**0.5
    return SD



def NMmethod(maxiteration):
    for i in range(0,maxiteration):
        oldp=P.copy()
        if sd() <1e-3 : return
        sort()
        x0=findx0()
        if not ReflectionExpansionandContraction(x0) : continue
        shrink()
        if np.array_equal(oldp,P):return

a=0.9
r=2
p=0.5
o=0.5
P=np.array([[-1,1],[10,1],[1,-1]])
NMmethod(int(1e2))
print(P)

