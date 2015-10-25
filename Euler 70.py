from primetools import sieve
from time import time

phi2 = lambda p1, p2: p1 * p2 - (p1 + p2 - 1)

primes = [2,3]
limit = 10**7
st = time()
sieve(limit ** (1/2) * 1.5, primes)
first = 0
minrat = 0
minratn = 0
for p1 in range(len(primes)):
    if primes[p1] ** 2 < limit: continue
    if first == 0: first = p1
    for p2 in range(first, -1, -1):
        t = primes[p1] * primes[p2] 
        if t > limit: continue
        p = phi2(primes[p1], primes[p2])
        if t / p > minrat and minrat > 0: break
        if sorted(str(p)) == sorted(str(t)):
            minrat = t/p 
            minratn = t 
            break
print(minratn)
print(time() - st)