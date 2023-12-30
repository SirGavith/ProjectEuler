def tryInt(n):
    for p in range(11, 20 + 1):
        if n % p != 0:
            return False;
    return True

i = 2
while True:
    print(i)
    if tryInt(i):
        print(i)
        break
    i += 1
