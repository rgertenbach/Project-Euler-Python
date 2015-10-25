import time
def remove_dupes(a):
    output = []
    for number in a:
        test = sorted(number)
        for i in range(len(test[:-1])):
            if test[i] == test[i + 1]: break
        else: output.append(number)
    return output

def join_arrays(a1, a2):
    output = []
    for e1 in a1:
        for e2 in a2:
            if e1[1:3] == e2[0:2]:
                output.append(e1[0] + e2)
    return remove_dupes(output)

start_time = time.time()
primes = [2,3,5,7,11,13,17]
multiples = []
for prime in range(len(primes)):
    multiples.append([])
    for i in range(1,1000):
        test = i * primes[prime]
        if test > 999: break
        if test < 100: multiples[prime].append("0" + str(test))
        else: multiples[prime].append(str(test))

for i in range(7): multiples[i] = remove_dupes(multiples[i])
working_array = multiples[6]

for i in range(5,-1,-1):
    working_array = join_arrays(multiples[i],working_array)


s = 0
for number in working_array:
    for i in range(1,10):
        if str(i) not in number:
            s += int(str(i) + number)
            break
print("--- %s seconds ---" % (time.time() - start_time))
print(s)
