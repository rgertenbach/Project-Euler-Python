"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

Do it for 1-20
"""

numbers = [x for x in range(2,10000)]

def sieve(n):
    prime = [2, 3]
    i = 3

    while prime[-1] < n:
        i += 2
        if i > n:
            break
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

def divisible(divisor, numbers):
    for number in numbers:
        if number % divisor == 0:
            return True
    return False

primes = sieve(numbers[-1])
result = []

for d in primes:
    while divisible(d, numbers):
        n = 0
        result.append(d)

        while n < len(numbers):
            if numbers[n] == d:
                numbers.pop(n)
            elif numbers[n] % d == 0:
                numbers[n] /= d
                n += 1
            else:
                n += 1

output = 1
for i in result:
    output *= i

print(output)