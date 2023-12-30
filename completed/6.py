n = 100

sumsquares = 0
sumsquared = 0
for i in range(1, n+1):
    sumsquared += i
    sumsquares += i**2

sumsquared = sumsquared ** 2

print(sumsquared, sumsquares, sumsquared - sumsquares)
