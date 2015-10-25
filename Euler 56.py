def digitsum(n):
   n = str(n)
   s = 0
   for digit in n:
       s += int(digit)
   return s

l = 0

for a in range(1,100):
   for b in range(100):
       if digitsum(a ** b) > l:
           l = digitsum(a ** b)

print(l)