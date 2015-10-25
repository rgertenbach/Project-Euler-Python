def sieve(n):
    prime = [2, 3]
    i = 3

    while i <= n:
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

    return prime

def factorial(n):
    r = 1
    for i in range(2, n + 1, 1): r *= i
    return r

def perm(arr, p):
    a = arr[:]
    l = len(a)
    p = p % factorial(l)
    output = []

    for d in range(l, 0, -1):
        f = factorial(d - 1)
        output.append(a.pop(p // f))
        p = p % f
    return output

def check_prime(number, primes):
    for prime in primes:
        if number % prime == 0: return False
        if prime ** 2 > number: return True
    return True

def aggregate(numbers):
    r = 0
    for number in numbers:
        r *= 10
        r += number
    return r

primes = sieve(31623)
numbers = [9,8,7,6,5,4,3,2,1]

for digits in range(9,4,-1):
    numbers.pop(0)
    for i in range(factorial(digits)):
        if check_prime(aggregate(perm(numbers, i)), primes):
            print(perm(numbers, i))
            break

