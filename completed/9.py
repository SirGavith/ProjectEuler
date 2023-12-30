import math
def isSquare(n):
    if int(math.sqrt(n))**2 == n:
        return True
    return False


found = False
a = 1
while a < 1000:
    if found: break
    b = a + 1
    while b < 1000:
        #print(a, b)
        if isSquare(a**2 + b**2):
            c = int(math.sqrt(a ** 2 + b ** 2))
            print("triplet", a, "+", b, "+", c, '=', a+b+c)
            if a+b+c == 1000:
                found = True
                print("product =", a*b*c)
                break
            elif a+b+c > 1000:
                break
        b += 1
    a += 1
