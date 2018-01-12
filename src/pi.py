import math
from math import *

def l(E):
    l = sqrt(2)
    for i in range(1,E+1):
        l = sqrt(2-2*sqrt(1-l*l/4))
    return l

c = l(15)*4*2**15

ipi = c/2
print(ipi)