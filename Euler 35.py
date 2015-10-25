def rotate(n):
    result = []
    number = str(n)
    for i in range(len(number)):
        number = number[1::] + number[0]
        result.append(int(number))
    return list(set(result))

def arrayin(a, b):
    for item in a:
        if item not in b: return False
    return True

def arrayappend(a, b):
    for item in a:
        b.append(item)
    return b

results = [2, 3]
prime = [2, 3]
i = 3

while i < 1000000:
    i += 2
    for j in prime:
        if j * j > i:
            prime.append(i)
            rotations = rotate(i)
            if arrayin(rotations, prime):
                results = arrayappend(rotations,results)
            break
        elif i % j == 0:
            break
        elif j == prime[-1]:
            break


print(len(results))
