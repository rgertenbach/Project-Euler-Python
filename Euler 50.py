def sieve(limit):
    primes = [2, 3]
    i = 3
    while i <= limit:
        i += 2
        for prime in primes:
            if i % prime == 0: break
            if prime ** 2 >= i:
                if i > limit:return primes
                primes.append(i)
                break
    return primes

def isprimes(number, primes):
    for prime in primes:
        if number % prime == 0: return False
        if prime ** 2 > number: return True


limit = 1000000
primes = sieve(limit)
l = len(primes)
primemax = 0
stepsmax = 0

for start in range(l):
    if primes[start] * stepsmax > limit: break
    for end in range(start + 2 + stepsmax, l):
        s = sum(primes[start:end])
        if s > limit: break
        if isprimes(s, primes):
            if end - start > stepsmax:
                stepsmax = end - start
                primemax = s
    if sum(primes[start:start + stepsmax]) > limit: break

print("%s with %s" % (primemax, stepsmax))