def isPandigital(number):
    digits=[str(digit) for digit in range(1,10)]
    if "0" in number: return False
    for digit in digits:
        count=0
        for position in number:
            if digit == position:
                count+=1
                if count > 1:
                    return False
        if count == 0:
            return False
    return True

def eligible(a,b= ""):
    test = str(a) + str(b)
    if "0" in test: return False
    test = sorted(test)
    for i in range(len(test) - 1):
        if test[i] == test[i + 1]: return False
    return True

s = []

for a in range(1,99):
    if not eligible(a): continue
    for b in range(123, 9876):
        if a >= 10:
            if b >= 5000: break
        if eligible(a,b):
            if isPandigital(str(a) + str(b) + str(a * b)):
                s.append(a * b)
s = set(s)
print(sum(s))