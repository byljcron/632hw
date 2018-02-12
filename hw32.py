import math
from matplotlib import pyplot


def func(x):
    return 1.0*math.exp(-x)

def trapezoidal(n,lower,upper):
    sum=0.0
    nth=1
    while nth<=n:
        x1=1.0*nth*upper/n
        x2=1.0*x1+upper/n
        sum=sum+(upper/n)*(func(x1)+func(x2))/2
        nth=nth+1
    return sum
result=[0]*10
for i in range (0,10):
    ith=math.pow(2,i)
    exat=0.63212055882
    result[i]=math.log(trapezoidal(ith,0,1))
    print(ith," ",trapezoidal(ith,0,1), " ", -(trapezoidal(ith,0,1)-exat)/exat)
pyplot.plot(result)
pyplot.show()
