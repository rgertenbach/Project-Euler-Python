"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sieve(n):
    prime = [2, 3]
    i = 3

    while prime[-1] < n:
        i += 2
        for j in prime:
            if j*j > i:
                prime.append(i)
                break
            elif i % j == 0:
                break
            elif j == prime[-1]:
                prime.append(i)
                break
    if prime[-1]>n:
        return sum(prime[:-1])
    else:
        return sum(prime[:])

print(sieve(2000000))