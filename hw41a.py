import math
from numpy import random
from matplotlib import pyplot

def generateGaussianNoise(mu,sigma):
   u1=random.random(1)
   u2=random.random(1)
   return  math.sqrt(-2.0 * math.log(u1)) * math.cos(math.pi*2 * u2)
result=[generateGaussianNoise(0,1)]
for a in range(0,10000):
    result.append(generateGaussianNoise(0,1))
pyplot.hist(result, bins='auto')
pyplot.show()
