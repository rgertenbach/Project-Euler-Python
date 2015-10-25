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