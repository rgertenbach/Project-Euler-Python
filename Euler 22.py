score = 0

f = open("E:\OneDrive\Python\Euler\Euler 22.txt", 'r')
for row in f:
    names = row.split(",")
    names.sort()
for i in range(len(names)):
    for letter in names[i][1:-1]:
        score += (i + 1) * (ord(letter) - 64)
print(score)