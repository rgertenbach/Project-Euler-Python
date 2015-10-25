def maxdiv(n):
    for i in range(1,n):
        if (i ** 2) > n: return i - 1
    return n - 1

def divsum(n):
    s = 0
    for i in range(1, maxdiv(n)+1):
        if n % i == 0:
            if i ** 2 == n or i == 1:
                s += i
            else:
                s += i
                s += n / i
    return int(s)

s = 0
for i in range(1,10000):
    if i == divsum(divsum(i)) and i != divsum(i):
        s += i
print("Result: %s" %s)