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