import random
from matplotlib import pyplot

import math

def func(x1,x2,x3,x4,x5,x6,x7,x8,x9,x0):
    return math.pow(x1+x2+x3+x4+x5+x6+x7+x8+x9+x0,2)

def check(x1,x2,x3,x4,x5,x6,x7,x8,x9,x0,y):
    if y<=func(x1,x2,x3,x4,x5,x6,x7,x8,x9,x0):
        return True
    else: return False

def inte (n):
    cnt=0
    for i in range(0,int(n)):
        x1=random.uniform(0,1)
        x2=random.uniform(0,1)
        x3=random.uniform(0,1)
        x4=random.uniform(0,1)
        x5=random.uniform(0,1)
        x6=random.uniform(0,1)
        x7=random.uniform(0,1)
        x8=random.uniform(0,1)
        x9=random.uniform(0,1)
        x0=random.uniform(0,1)
        y=random.uniform(0,100)
        if check(x1,x2,x3,x4,x5,x6,x7,x8,x9,x0,y):cnt=cnt+1
    return 100.0*cnt/n
n=17
result=[0]*17
error=[0]*17
xaxis=[0]*17
for nth in range(1,n):
    xaxis[nth]=1.0/math.sqrt(math.pow(2,nth))
    result[nth]=inte(math.pow(2,nth))
    error[nth]=abs((result[nth]-155.0/6)/(155.0/6))
    print(nth,result[nth],error[nth])

pyplot.scatter(xaxis,error)
pyplot.show()
