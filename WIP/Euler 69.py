def sieve(limit):
    i = primes[-1]
    while i * 2 <= limit:
        i += 2
        for prime in primes:
            if i % prime == 0: break
            if prime ** 2 >= i: 
                if i > limit: return primes
                primes.append(i)
                break                        


def primefactors(n):
    factors = []
    sieve(n)
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n /= prime 
        if n == 1: return factors
    if factors == []: return n 


def crossproducts(n):
    factors = primefactors(n)
    indices = []
    indices.append([[i] for i in range(len(factors))])
    
    for i in range(1,len(factors)-1):
        indices.append([])
        for e in indices[-2]:
            for factor in range(len(factors)):
                if factor not in e and factor > max(e):
                    indices[-1].append(e + [factor])
                    
    multiples = []
    for level in indices:
        for set in level:
            multiples.append(1)
            for index in set:
                multiples[-1] *= factors[index]
                        
    return multiples


def phi(n):
    relative_primes = n - len(set(crossproducts(n)))
    return relative_primes



primes = [2,3]
i=680
print(primefactors(680))
print(crossproducts(i))
print(phi(i))


print("done")