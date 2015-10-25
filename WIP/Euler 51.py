import time
from primetools import is_prime
st = time.time()
tt = 0
pri = 8

def replace(input, rep, d1, d2):
    return input[:d1] + rep + input[d1 + 1: d2] + rep + input[d2 + 1:]

def change(n):
    n = str(n)
    for p1 in range(len(n) - 2):
        if int(n[p1]) > 10 - pri: continue
        for p2 in range(p1 + 1, len(n)-1):
            if n[p1] == n[p2]:
                c = 0
                for i in range(10):
                    if (10 - i) - (pri - c) < 0: break
                    if p1 == 0 and i == 0: continue
                    if int(n[p1]) > i: continue
                    if is_prime(int(replace(n, str(i), p1, p2)), primes): c += 1
                if c == pri: return True
    return False

def nextprime(prime, checkprimes):
    n = prime + 2
    while not is_prime(n, checkprimes): n +=2
    return n 

primes = [2, 3]
prime = 3

while not change(prime):
    st1 = time.time()
    prime = nextprime(prime, primes)
    tt += time.time() - st1

print(prime)
print(time.time() - st)
