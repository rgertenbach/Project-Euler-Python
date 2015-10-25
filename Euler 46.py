def sieve(limit):
    i = primes[-1]
    
    while i <= limit:
        i += 2
        for prime in primes:
            if i % prime == 0: break
            if prime ** 2 >= i: 
                if i > limit: return primes
                primes.append(i)
                break                        
   
def composite(n):
    for prime in primes:
        if n % prime == 0: return True
    return False

def gold(n):
    for prime in primes:
        if (((n - prime) / 2) ** (1 / 2)) % 1 == 0: return True
    return False

primes = [2, 3, 5, 7]
n = 7

while True:
    n += 2
    sieve(n)
    if composite(n):
        if not gold(n): break
    
print(n)
