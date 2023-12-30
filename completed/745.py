import math, sympy, numpy, time
from functools import lru_cache

n = 100

@lru_cache()
def jordan(n):
    a = n ** 2; 
    for p in sympy.ntheory.factor_.divisors(n):
        if (sympy.isprime(p)):
            a *= 1 - 1 / (p ** 2)
    return math.floor(a)

begin = time.time()
sum = 0
for i in range(math.floor(math.sqrt(n))):
    i += 1
    sum += math.floor(n/i ** 2) * jordan(i)
    sum %= 1000000007
    if (i % 1000 == 0):
        print(i, sum)

print("Sum:", sum)
print(time.time()-begin)

print(sympy.ntheory.factor_.divisors(9))