def reduce(n, d):
    i = 2
    while i <= n:
        if n % i == 0 and d % i==0:
            n /= i 
            d /= i 
        else: i += 1
    return n, d


def nom(d):
    return int(d * 3 / 7)

closest = 2/5
closestn = 0
closestd = 0


for d in range(500001, 1000001):
    if nom(d)/d > closest and d*3/7 % 1 > 0: 
        closest = int(d*3/7)/d 
        closestd = d 
        closestn = int(d*3/7) 
print(reduce(closestn,closestd))