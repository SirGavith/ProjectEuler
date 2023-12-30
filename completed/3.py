import sympy
n = 600851475143
pfactors = []
for p in sympy.ntheory.factor_.divisors(n):
    if (sympy.isprime(p)):
        pfactors.append(p)
pfactors.sort()
print(pfactors[-1])
