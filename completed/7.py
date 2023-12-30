import sympy

primeth = 0
n = 0
while True:
    if sympy.isprime(n):
        if primeth == 10001 - 1:
            print(n)
            break
        primeth += 1
    n += 1
