import primetools
import time

start_time = time.time()
primes = [2, 3]

def merge(a,b):
    return int(str(a) + str(b)), int(str(b) + str(a))

def areprime(a):
    return primetools.is_prime(a[0], primes) and primetools.is_prime(a[1], primes)
    
def primechainsum(chains, primes):
    for chain in chains:
        if len(chain) == primes: return sum(chain)
    return 0    


# check against every prime in every array and add if applicable
n = 2 # the latest prime to be checked
ptc = 5
chains = []
primecandidates = []
tt1 = 0


while primechainsum(chains, ptc) == 0:
    if n == primes[-1]: primetools.sieve(len(primes) + 1, primes, True)
    n = primes[primes.index(n) + 1]
    primecandidates = []
    
    for prime in primes:
        if areprime(merge(n, prime)): primecandidates.append(prime)
    
    for chain in chains:
        allmatch = True
        for prime in chain:
            if prime not in primecandidates:
                allmatch = False
                break
        if allmatch: chains.append(chain + [n])
    chains.append([n])
    
print(primechainsum(chains, ptc))
print(time.time() - start_time)