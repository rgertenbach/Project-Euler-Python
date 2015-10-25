def value(word):
    return sum([ord(letter) - 64 for letter in word])

def gen_triangles(existing, limit):
    while existing[-1] < limit:
        t = len(existing) + 1
        existing.append(t * (t + 1) / 2)
triangle_words = 0
triangles = [1]
with open("E:\OneDrive\Python\Euler\Text Files\Euler 42.txt", 'r') as f:
    for line in f: words = line.split(",")
for word in words:
    v = value(word[1:-1])
    if v > triangles[-1]: gen_triangles(triangles, v)
    if v in triangles: triangle_words += 1
print(triangle_words)
