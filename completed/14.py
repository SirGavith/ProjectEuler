def seqlen(n):
    len = 0
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
        len += 1
    return len + 1



longestseq = [0,0]
for i in range(1000000):
    l = seqlen(i)
    if l >  longestseq[0]:
        longestseq = [l, i]
    print(i, l)

print(longestseq)
print(longestseq[1])