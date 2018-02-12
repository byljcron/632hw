from scipy import integrate
from scipy.special import erf
from matplotlib import pyplot
import math

def func(x):
     return 1.0*math.exp(-x)
result = integrate.romberg(func, 0, 1,divmax=500,show=True)
