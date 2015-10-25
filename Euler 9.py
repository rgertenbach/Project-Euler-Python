limit = 1000

def find_triplet():
    for a in range(1, limit - 3):
        for b in range(1,limit - a - 1):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a*b*c

print(find_triplet())