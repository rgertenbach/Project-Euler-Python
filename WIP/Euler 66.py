xmax = 0

def dioph(d):



for d in range(2, 100):
    y = 0
    if d ** (1 / 2) % 1 == 0: continue
    while True:
        y += 1
        t = d * y ** 2 + 1
        if t ** (1 / 2) % 1 == 0: break
        xmax = t ** (1 / 2)

print(xmax)
