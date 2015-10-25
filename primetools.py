def sieve(limit = 0, primes = [2, 3], nth = False):
    i = primes[-1]
    
    while (len(primes) if nth else i) < limit:
        i += 2
        for prime in primes:
            if i % prime == 0: break
            if prime ** 2 > i: 
                if (False if nth else i > limit): return primes[-1]
                primes.append(i)
                break 
                                       
    return primes[-1]

def is_prime(n, primes = None):
    if primes == None: primes = [2, 3]
    sieve(n ** (1 / 2), primes)
    for prime in primes:
        if n % prime == 0: return False
        if prime ** 2 > n: return True
    return True