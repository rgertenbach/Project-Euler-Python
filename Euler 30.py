def build_number(a):
    output = 0
    zeros = 0
    for digit in a:
        if digit == 0: zeros += 1
        elif digit > -1:
            output *= 10
            output += digit
    return output * 10 ** zeros

def increase_array(a):
    for d in range(1, len(a) + 1):
        if a[-d] < 9:
            if a[-d] == -1: a[-d] = 0
            else: a[-d] += 1
            break
    for i in range(1,d):
        a[- (d - i)] = a[-d]
    return 0

def compare(n1, n2):
    if sorted(str(n1)) == sorted(str(n2)): return True
    return False

def sumpow(a):
    s = 0
    for digit in a:
        if digit == -1: continue
        s += digit ** 5
    return s

s = 0
numbers = [-1, -1, -1, -1, -1, 2]
while numbers != [2, 3, 4, 4, 5, 9]:
    increase_array(numbers)
    if compare(build_number(numbers), sumpow(numbers)):
        s += sumpow(numbers)
print(s)