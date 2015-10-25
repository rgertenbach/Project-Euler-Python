def lyc(n):
    n = str(n)
    c = 1
    n = str(int(n) + int(n[::-1]))
    while n != n[::-1] and c < 50:
        c += 1
        n = str(int(n) + int(n[::-1]))
    if c == 50: return 1
    return 0

l = 0
for i in range(1,10000):
    l += lyc(i)
print(l)