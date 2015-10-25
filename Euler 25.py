a = 0
b = 1
c = 1
i = 2
while len(str(c)) < 1000:
    a = b
    b = c
    c = a + b
    i += 1
print(i)