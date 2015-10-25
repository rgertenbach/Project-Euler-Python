def divide(n, d):
    n *= 10
    r = n % d  # remainder
    n = n // d # result
    return n,r


def calc_steps(d):
    n = 1
    steps = []

    while n > 0:
        step = divide(n, d)
        if step in steps: break
        steps.append(step)
        n = step[1]
    return steps[steps.index(step):]

longest = 0
longestd = 0
for d in range(1, 1000):
    steps = calc_steps(d)
    if len(steps) > longest:
        longest = len(steps)
        longestd = d
print(longestd)