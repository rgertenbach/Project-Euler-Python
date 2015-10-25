import time
start_time = time.time()
from functools import reduce

hyp = lambda a,b: (a**2 + b**2)**(1/2)

def triangles(limit):
    c = {}
    for a in range(1, int(limit / 2)):
        for b in range(1, a):
            if hyp(a,b)%1 == 0:
                l = hyp(a,b) + a + b
                if l <= 1000:
                    if c.get(l) == None:
                        c[l] = 1
                    else: c[l] += 1
    return c


t = triangles(1000)
print(reduce(lambda x,y: x if t[x] > t[y] else y, t.keys()))

print("--- %s seconds ---" % (time.time() - start_time))
