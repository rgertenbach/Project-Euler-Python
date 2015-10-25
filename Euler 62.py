def propsort(n):
    n = sorted(str(n)) 
    o = ""
    for letter in n: o += letter
    return o    

def countcubes(a):
    cc = {}
    for c in [propsort(c) for c in a]:
        if c not in list(cc.keys()):
            cc[c] = 1
        else: cc[c] += 1
  
    for cube in cc.items():
        if cube[1] == 5:
            for c in a:
                if propsort(c) == cube[0]:
                    return c 
    return 0

i = 2
cubes = [1]

while True:
    while len(str(cubes[0])) == len(str(i**3)):
        cubes.append(i ** 3)
        i += 1
    c = countcubes(cubes)
    if c == 0:
        cubes = [i ** 3]
        i += 1
    else: break
print(c)
print("done")