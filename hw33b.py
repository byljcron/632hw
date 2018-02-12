from scipy import integrate
from scipy.special import erf
from matplotlib import pyplot
import math

def func(x):
     return math.pow(math.sin(x),2)

def h(n):
    return 1/pow(2,n)*(4*math.pi)

def R(n,m):
    if  m is 0:
        if n is 0:
            return h(1)*(func(0)+func(4*math.pi))
        else:
            rn0=1.0/2*R(n-1,0)
            hn=h(n)
            tmp=0
            for k in range(1,int(math.pow(2,n-1))+1):
                tmp=tmp+func(0+(2*k-1)*hn)
            return rn0+hn*tmp
    return 1.0/(math.pow(4,m)-1)*(math.pow(4,m)*(R(n,m-1)-R(n-1,m-1)))

diff=100
n=3
while diff>0.00001:
   Rn=R(n,n)
   Rn1=R(n-1,n-1)
   diff=abs(Rn-Rn1)
   n=n+1
   print(n,Rn,Rn1,diff)
