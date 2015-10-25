n = 600851475143
prime = [2, 3]
i=3
while n > prime[len(prime)-1]:
    i += 2
    for j in prime:
        if j * j > i:
            prime.append(i)
            break
        elif i % j == 0:
            break
        elif j == prime[len(prime) - 1]:
            prime.append(i)
            break

    if n % i == 0:
        n = n / i

print (prime[len(prime)-1])