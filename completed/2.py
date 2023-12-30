
fibs = [0, 1]
sum = 0
i = 0
while fibs[-1] < 4000000:
    f = fibs.copy()
    fibs[0] = f[1]
    fibs[1] =f[0] + f[1]
    print(fibs)
    if (fibs[1] % 2 == 0):
        sum += fibs[1]
print(sum)
