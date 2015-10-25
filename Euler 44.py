def pent(i):
    return i * (3 * i - 1) / 2

i = 2
pents = [1, 5]
result = 0

while result ==0:
    i += 1
    pents.append(pent(i))
    s = pents[-1]
    for element in pents:
        if element > s/2: break
        element2 = s - element
        if element2 in pents:
            if element2 - element in pents:
                result = element2 - element
                break
print(result)