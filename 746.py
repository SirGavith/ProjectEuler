import math, sympy, time, itertools
import numpy as np
from functools import lru_cache

@lru_cache
def M(n):
    #permutations
    family = np.array([0,1,0,1])
    table = np.repeat(family, n + 1)
    print(n, table)
        
    p = itertools.permutations(table)
    print(set(list(p)))
    return 0

n = 3
sum = 0
for i in range(2,n):
    sum += M(i)
    sum %= 1000000007
print(sum)
