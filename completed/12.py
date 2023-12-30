import sympy
triangle = 0
i = 1
while True:
    triangle += i
    if (len( sympy.divisors(triangle)) > 500):
        print(triangle)
        break
    i += 1