gridsize = 1001
levels = gridsize // 2 + 1

current = 1
total = 1

for level in range(1, levels):
    for i in range(4):
        current += level * 2
        total += current

print(total)