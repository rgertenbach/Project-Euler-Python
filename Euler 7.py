"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def sieve(n):
    prime = [2, 3]
    i = 3

    while len(prime) < n:
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

    return prime[-1]

print(sieve(10001))
