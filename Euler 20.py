def fact(n):
    if n == 1: return 1
    return n * fact(n-1)

test = str.fact(10))
result = 0
for digit in test:
    result += int(digit)

print(result)