import time
start_time = time.time()

def append_corners(layer):
    corners[0] = corners[3] + layer * 2
    corners[1] = corners[0] + layer * 2
    corners[2] = corners[1] + layer * 2
    corners[3] = corners[2] + layer * 2
        
def sieve(limit):
    i = primes[-1]
    while primes[-1] ** 2 <= limit:
        i += 2
        for prime in primes:
            if i % prime == 0: break
            if prime ** 2 > i: 
                #if i > limit: return 0 # yolo
                primes.append(i)
                break                        
    
def isprime(n):
    for i in primes:
        if n % i == 0: return False
        if i ** 2 > n: return True
           
def prime_density():

    p = 0
    for n in corners[:3:]:
        if isprime(n): 
            p += 1
    return p
    
corners = [0,0,0,1]
primes = [2, 3]
layer = 0
p = 0
np = 1

while True:
    layer += 1
    append_corners(layer)
    sieve(corners[-1])
    p += prime_density()
    np += 4
    if p / np < .1: break
print(layer * 2 + 1)
print("--- %s seconds ---" % (time.time() - start_time))