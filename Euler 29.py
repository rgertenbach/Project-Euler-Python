results = []
for i in range(2,101):
    for k in range(2,101):
        results.append(i ** k)
results = set(results)
print(len(results))