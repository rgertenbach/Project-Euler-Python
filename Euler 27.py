import time
start_time = time.time()

def sieve(n, prime):
    i = prime[-1]

    while prime[-1] < n :
        i += 2
        if i > n: break
        for j in prime:
            if j*j > i:
                prime.append(i)
                break
            elif i % j == 0:
                break
            elif j == prime[-1]:
                prime.append(i)
                break
    return 0



def inprimes(n, a, b, primes):
    test = n ** 2 + a * n + b
    if test > primes[-1]:
        sieve(test, primes)

    if test in primes: return True
    return False




primes = [2,3]
sieve(1000, primes)
maxconsec = 0
maxprod = 0

for a in range(-999,1000,1):
    for b in [x for x in primes if x < 1000]:
        n = 1
        consec = 1
        while inprimes(n, a, b, primes):
            consec += 1
            n += 1
        if consec > maxconsec:
            maxconsec = consec
            maxprod = a * b
print(maxprod)
print("--- %s seconds ---" % (time.time() - start_time))