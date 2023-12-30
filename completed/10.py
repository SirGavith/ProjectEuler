import sympy
n = 2000000
sum = 0
for i in range(n):
    if sympy.isprime(i):
        sum += i

print(sum)