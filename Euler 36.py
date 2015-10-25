import time
start_time = time.time()

def binary(n):
    return str(bin(n)[2::])

def create_palimdrome(n, mirror):
    n = str(n)
    if mirror: return n + n[::-1]
    return n + n[len(n)-2::-1]

def is_pal(n):
    n = str(n)
    return n == n[::-1]



s = 1
n = 1
m = False
c = 0
while True:
    test = create_palimdrome(binary(n), m)
    if int(test, 2) > 10000000000: break
    test2 = int(test, 2)
    if test2 >= 1000000:
        c += 1
        if c == 4: break
    if is_pal(test2) and test2 < 1000000:
        s += test2
    m = not m
    if m == False: n += 1


s -= 3 # 3 three comes twice and one is excluded
print(s)
print("--- %s seconds ---" % (time.time() - start_time))