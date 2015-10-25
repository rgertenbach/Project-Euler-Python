def arrayin(a, b):
    for item in a:
        if item not in b: return False
    return True

def truncate(n):
    number = str(n)
    result = []

    for i in range(len(number)-1):
        result.append(int(number[0:len(number) - i - 1:]))
        result.append(int(number[i + 1::]))

    return list(set(result))


result = []
prime = [2, 3, 5, 7, 11, 13]
i = 13

while len(result) < 11:
    i += 2
    for j in prime:
        if j * j > i:
            prime.append(i)
            truncations = truncate(i)
            if arrayin(truncations, prime):
                result.append(i)
            break
        elif i % j == 0:
            break
        elif j == prime[-1]:
            break

print(sum(result))