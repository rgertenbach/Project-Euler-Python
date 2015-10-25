def check_m(n, maxmult):
   base = sorted(str(n))
   for i in range(2, maxmult + 1):
       if sorted(str(n * i)) != base: return False
   return True

n = 1
while not check_m(n, 6):
   n += 1

print(n)