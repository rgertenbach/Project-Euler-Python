ways = [0 for x in range(201)]
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways[0] = 1

for i in range(len(coins)):
    for j in range(coins[i], len(ways)):
        ways[j] += ways[j - coins[i]]

print(ways[-1])
