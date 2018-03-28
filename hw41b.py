import math
from numpy import random
from matplotlib import pyplot
def possion(x,mu,sigma):
    return math.exp(-math.pow((x-mu),2)/(sigma*sigma*2))/(sigma*math.pow(2*math.pi,0.5))

def vonmethod(mu,sigma):
    W=random.random(1)
    x=random.uniform(-10,10)
    if W>possion(x,mu,sigma):
        return vonmethod(mu,sigma)
    else:
        return x

result=[vonmethod(0,1)]
for a in range(0,10000):
    result.append(vonmethod(0,1))
pyplot.hist(result, bins='auto')
pyplot.show()

