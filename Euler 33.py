fraction = []
for a in range(10, 100):
    for b in range(a + 1, 100):
        if b % 10 == 0: continue
        if str(a)[1] == str(b)[0]:
            if int(str(a)[0]) / int(str(b)[1]) == a / b:
                fraction.append([a, b])
result = [1, 1]

for f in fraction:
    result[0] *= f[0]
    result[1] *= f[1]

for i in range(2, result[0]):
    if i > result[0]: break
    while result[0] % i == 0 and result[1] % i == 0:
        result[0] /= i
        result[1] /= i
print(result[1])