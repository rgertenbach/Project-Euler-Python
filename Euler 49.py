def sieve(limit):
    primes = [2, 3]
    i = 3
    while i<= limit:
        i+= 2
        for prime in primes:
            if i % prime == 0: break
            if prime ** 2 >= i:
                if i> limit:return primes
                primes.append(i)
                break
    return primes

def arraytostr(a):
    output = ""
    for number in a: output += number
    return output

primes = sieve(9999)
primes = [prime for prime in primes if prime > 1000]
primesperms = [arraytostr(sorted(str(prime))) for prime in primes]
uniqueperms = list(set(primesperms))
uniquepermscounts =[]
for uniqueperm in uniqueperms:
    i = 0
    for perm in primesperms:
        if perm == uniqueperm: i += 1
    uniquepermscounts.append(i)

for i in range(len(uniqueperms)):
    if uniquepermscounts[i] >= 3:
        perms = []
        for k in range(len(primesperms)):
            if primesperms[k] == uniqueperms[i]:
                perms.append(primes[k])
        for k in range(len(perms) - 2):
            if perms[k + 1] - perms[k] == perms[k + 2] - perms[k + 1]:
                print(str(perms[k]) + str(perms[k + 1]) + str(perms[k + 2]))
