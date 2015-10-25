fracts = [(1,2)]
for i in range(1,1000):
   fracts.append((fracts[i-1][1], 2 * fracts[i-1][1] + fracts[i-1][0]))

c = 0
for fract in fracts:
   if len(str(fract[0] + fract[1])) > len(str(fract[1])):
       c += 1

print(c)