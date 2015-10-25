import time
start_time = time.time()

def powerlength(ll, b):
    lowerlimit = ll 
    c = 0
    
    for a in range(ll, 10):
        t = a ** b 
        if len(str(t)) < b: lowerlimit += 1
        if len(str(t)) == b: c += 1
        
    if lowerlimit == 10: return c, -1
    return c, lowerlimit

exp = 0
base = 1
lowerlimit = 1
c = 0
while True:
    exp += 1
    r = powerlength(lowerlimit, exp)
    c += r[0]
    lowerlimit = r[1]
    if lowerlimit == -1: break
print(c)
print("--- %s seconds ---" % (time.time() - start_time))