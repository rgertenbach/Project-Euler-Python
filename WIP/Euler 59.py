f = open ("E:\OneDrive\Python\Euler\Text Files\Euler 59.txt", "r")
file = f.readline().split(",")
for l1 in range(26):
    for l2 in range(26):
        for l3 in range(26):
    print("".join([chr(int(x) ^ 97 + letter1) for x in file]))
f.close()
