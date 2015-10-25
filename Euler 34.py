def factorial(n):
    result = 1
    for i in range(2, n + 1): result *= i
    return result

def fact_sum(a):
    s = 0
    for number in a:
        if number > -1:
            s += factorial(number)
    return s

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

def count_0(n, a):
    return sum([d == '0' for d in str(n)]) == sum([d == 0 for d in a])

numbers = [-1, -1, -1, -1, -1, -1, 2]
s = 0
while numbers != [0, 0, 1, 2, 4, 5, 6]:
    increase_array(numbers)
    test = fact_sum(numbers)
    if compare(test, build_number(numbers)):
        if count_0(test, numbers):
            s += test
print(s)