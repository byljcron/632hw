import numpy as np
import matplotlib.pyplot as plt


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

def drawgraph():
    x = np.linspace(-1, 1.5, 256)
    y = np.linspace(-1, 1.5, 256)
    X,Y = np.meshgrid(x, y)
    Z = Rosenbrock([X, Y])

    fig, ax = plt.subplots()

    cnt = plt.contour(X,Y,Z,8,   extent=[0, 1, 0, 1])
    axes = plt.gca()
    axes.set_xlim([-1,1.5])
    axes.set_ylim([-1,1.5])
    plt.plot([P[0][0],P[1][0]], [P[0][1],P[1][1]],linewidth=1, linestyle='-',marker="o")
    plt.plot([P[2][0],P[1][0]], [P[2][1],P[1][1]],linewidth=1, linestyle='-',marker="o")
    plt.plot([P[0][0],P[2][0]], [P[0][1],P[2][1]],linewidth=1, linestyle='-',marker="o")
    plt.show()


def NMmethod(maxiteration):
    global P
    for i in range(0,maxiteration):
        print(P[0],P[1],"f(x1):",Rosenbrock(P[0]),"f(x2):",Rosenbrock(P[1]),"f(x3):",Rosenbrock(P[2]))
        drawgraph()
        oldp=P.copy()
        if sd() <1e-3 : return
        sort()
        x0=findx0()
        if not ReflectionExpansionandContraction(x0) : continue
        shrink()
        if np.array_equal([oldp[0],oldp[1]],[P[0],P[1]]):return

a=0.9
r=2
p=0.5
o=0.5
P=np.array([[-1,1],[10,1],[1,-1]])
NMmethod(int(1e2))
print(P)

