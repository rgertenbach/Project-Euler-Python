def lin_mult(n):
    for i in range(1,5):
        test = n[:]
        base = int(n[:i])
        test = test[i:]
        m = 1
        while len(test) > 0:
            m += 1
            if str(base*m) == test[:len(str(base*m))]:
                test = test[len(str(base*m)):]
            else: break
        if len(test) == 0: return True
    return False

def factorial(n):
    r = 1
    for i in range(2, n + 1, 1): r *= i
    return r

def perm(arr, p):
    a = arr[:]
    l = len(a)
    p = p % factorial(l)
    output = []

    for d in range(l, 0, -1):
        f = factorial(d - 1)
        output.append(a.pop(p // f))
        p = p % f
    return output

def buildnum(n):
    o = ""
    for e in n: o += str(e)
    return o
    
numbers = [9,8,7,6,5,4,3,2,1]
i = 0

while not lin_mult(buildnum(perm(numbers, i))):
    i += 1
    
print(buildnum(perm(numbers,i)))