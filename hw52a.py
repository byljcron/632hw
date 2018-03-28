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




result=[RnC()]
for a in range(0,1000):
    result.append(RnC())
for i in range(1,8):
    print(2**i,mle(2**i))
print(500,mle(500))
print(1000,mle(1000))
plt.hist(result, bins='auto')
plt.show()


