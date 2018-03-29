import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.optimize as opt

def func(m):
    return 1.0/((m-0.8)**2+0.25)

def RnC():
   P=np.random.random()
   m=np.random.random()*5
   if P<=func(m):
       return float(m)
   else:
       return RnC()
def dLdx(x,n):
#log likelihood
    global result
    L=0
    for i in range(0,n):
        L=L+2*(result[i]-x)/(0.25+(result[i]-x)**2)
    return abs(L)
def mle(n):
    mleresult= opt.minimize(dLdx,0.8,n,method = 'Nelder-Mead')
    if mleresult.success:
        return mleresult.x
    else:
        return False

def uncertainty(n,x):
    global result
    dab=0
    for i in range(0,n):
        dab=dab+(2* (-0.25 + (result[i] - x)**2))/(0.25 + (result[i] - x)**2)**2
    return -1.0/dab


result=[RnC()]
for a in range(0,1000):
    result.append(RnC())
for i in range(1,8):
    print(2**i,mle(2**i),uncertainty(2**i,mle(2**i)))
print(500,mle(500),uncertainty(500,mle(500)))
print(1000,mle(1000),uncertainty(1000,mle(1000)))
#plt.hist(result, bins='auto')
d = np.arange(0.0, 5.0, 0.01)
plt.plot(d,func(d))
plt.axvline(x=uncertainty(64,mle(64))+0.8, color='r', linestyle='-')
plt.axvline(x=uncertainty(1000,mle(1000))+0.8, color='b', linestyle='-')
plt.show()


