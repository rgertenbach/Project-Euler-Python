def crossproducts(factors):
    indices = []
    indices.append([[i] for i in range(len(factors))])
    
    for i in range(1,len(factors)):
        indices.append([])
        for e in indices[-2]:
            for factor in range(max(e)+1,len(factors)):
                if factor not in e :
                    indices[-1].append(e + [factor])
                    
    multiples = []
    for level in indices:
        for set in level:
            multiples.append(1)
            for index in set:
                multiples[-1] *= factors[index]
    return multiples