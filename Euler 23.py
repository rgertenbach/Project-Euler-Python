import time
start_time = time.time()


def sieve(n):
    prime = [2, 3]
    i = 3

    while True:
        i += 2
        if i * i > n: break
        for j in prime:
            if j*j > i:
                prime.append(i)
                break
            elif i % j == 0:
                break
            elif j == prime[-1]:
                prime.append(i)
                break
    return prime
"""
def sumdiv(n):
    s = 1
    multiples = []
    for prime in primes:
        if s > n: return s # not proper sumdiv
        elif prime * prime > n: return s
        elif prime * prime == n:
            s += prime
            return s
        elif n % prime == 0:
            s += prime
            s += n / prime
            number = prime * 2
            while number * number <= n:
                if(number in multiples): break
                multiples.append(number)
                if number * number == n: s += number
                elif n % number == 0:
                    s += number
                    s += n / number
                number += prime
    return s
"""

def sumdiv(n):
    s = 1
    for div in range(2, n):
        if div ** 2 > n: break
        if div ** 2 == n: return s + div
        if n % div == 0:
            s += div
            s += n / div
    return s

primes = sieve(28123)
abundant = []
ab_sums = []
for i in range(12, 28123 - 11):
    if sumdiv(i) > i: abundant.append(i)

for ab1 in range(len(abundant)):
    for ab2 in range(ab1, len(abundant)):
        value = abundant[ab1] + abundant[ab2]
        if value > 28123: break
        ab_sums.append(value)

ab_sums = list(set(ab_sums))
print(28123 * 28124 / 2 - sum(ab_sums))
print("--- %s seconds ---" % (time.time() - start_time))
