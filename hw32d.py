import random
from matplotlib import pyplot

import math

def func(x):
    return 1.0*math.exp(-x)

def check(x,y):
    if y<=func(x):
        return True
    else: return False

def inte (n):
    cnt=0
    for i in range(0,n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if check(x,y):cnt=cnt+1
    return 1.0*cnt/n
n=[10,20,50,100,200,500,1000,2000,5000,10000]
result=n
i=0
for nth in n:
    result[i]=inte(nth)
    print(nth,result[i],abs((result[i]-0.63212055882)/0.63212055882))
    i=i+1
pyplot.plot(result)
pyplot.show()
