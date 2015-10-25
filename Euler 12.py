def divisors(num, primes):
    if num == 1:
        return 1
    elif num == 2: return 2
    else:
        divisors = 2
        divlist = [1, num]

    for divisor in primes:
        if divisor ** 2 <= num:
            if num % divisor == 0:
                if divisor ** 2 == num:
                    divisors += 1
                    divlist.append(divisor)
                else:
                    multiple = 0
                    while True:
                        multiple += divisor
                        if multiple ** 2 > num: break
                        if multiple ** 2 == num and multiple not in divlist:
                            divisors += 1
                            divlist.append(multiple)
                        elif num % multiple == 0 and multiple not in divlist:
                            divisors += 2
                            divlist.append(multiple)
                            divlist.append(num // multiple)
        else: break
    return divisors

def sieve(n, existing = []):
    if existing == []: result = [2]
    else: result = existing
    divisor = 3
    while divisor <= n:
        isprime = True
        for prime in result:
            if divisor % prime == 0:
                isprime = False
                break
        if isprime: result.append(divisor)
        divisor += 2
    return result

i = 1
triangle = 1
primes = sieve(1000)
while divisors(triangle, primes) <= 500:
    i += 1
    triangle += i

print (triangle)