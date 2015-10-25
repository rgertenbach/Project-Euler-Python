import time
start_time = time.time()

def factorial(n):
    r = 1
    for i in range(1,n + 1):
        r *= i 
    return r 

def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

g1m = 0    
for n in range(10,101):
    had = False
    for r in range(1, n):
        if ncr(n, r) > 1000000: 
            g1m += 1
            had = True
        elif had: break
        
print(g1m)
print("--- %s seconds ---" % (time.time() - start_time))