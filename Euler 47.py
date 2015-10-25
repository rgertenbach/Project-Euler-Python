def sieve(limit, primes):
    i = primes[-1]
    while i <= limit:
        i += 2
        for prime in primes:
            if i % prime == 0: break
            if prime ** 2 >= i:
                if i > limit: return primes
                primes.append(i)
                break
    return 0

def primefactors(number, primes):
    factors = 0
    for prime in primes:
        if number == 0: return factors
        if number % prime == 0:
            factors += 1
            while number % prime == 0:
                number /= prime
    return factors

primes = [2, 3]
sieve(1000, primes)
threshold = 4
consecutive = 0
start = 0
i = 0

while consecutive < threshold:
    i += 1
    if i > primes[-1]: sieve(i, primes)
    if primefactors(i, primes) == threshold:
        if start == 0: start = i
        consecutive += 1
    else:
        consecutive = 0
        start = 0
print(start)