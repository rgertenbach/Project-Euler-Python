import time
start_time = time.time()

def isin(n, a):
    for e in a:
        if e[1] == n: return True
    return False

def smartmerge(a1, a2):
    output = []
    for e in a2:
        if a1[-1][0][2:] == e[0][:2] and not isin(e[1], a1):
            output.append(a1 + [e])
    return output
            

def match(n, a):
    for e in a:
        if e[:2] == n[2:] or e[2:] == n[:2]:
            return True
    return False

gen = [lambda n: n * (n + 1) / 2,
       lambda n: n ** 2,
       lambda n: n * (3 * n - 1) / 2,
       lambda n: n * (2 * n - 1),
       lambda n: n * (5 * n - 3) / 2,
       lambda n: n * (3 * n - 2)
       ]

n = 0
values = []
pairs = []
carryover = []
while True:
    n += 1
    s = [f(n) for f in gen]
    if s[0] > 9999: break
    for i in range(6):
        if s[i] > 999 and s[i] <= 9999:
            if i == 5: pairs.append([(str(int(s[i])),i)])
            else: values.append((str(int(s[i])),i))

for i in range(5):
    for pair in pairs:
        temp = smartmerge(pair, values)
        for x in temp: carryover.append(x)
    pairs = carryover
    carryover = []

for pair in pairs:
    if pair[-1][0][2:] == pair[0][0][:2]: break

print(sum([int(x[0]) for x in pair]))
print("--- %s seconds ---" % (time.time() - start_time))