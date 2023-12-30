import sympy




def isPalindrome(n):
    n = str(n)
    if len(n) <= 1:
        return True
    if (n[0] == n[-1]):
        if isPalindrome(n[1:-1]):
            return True
    return False


palins = []
for p in range(10, 1000):
    for l in range(10, 1000):
        if (isPalindrome(p * l)):
            palins.append(p * l)

palins.sort()

print(palins)
