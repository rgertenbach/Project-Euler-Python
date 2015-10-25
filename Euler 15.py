"""
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20*20 grid?
"""

n = 20
lattice = []

for i in range (1, n + 1):
    lattice.append([])
    for j in range(1, n + 1):
        if i == 1:
            lattice[i - 1].append(j + 1)
        elif i > j:
            lattice[i - 1].append(0)
        elif i == j:
            lattice[i - 1].append(lattice[i - 2][j - 1]*2)
        else:
            lattice[i - 1].append(lattice[i - 2][j - 1] + lattice[i - 1][j - 2])

print (lattice[n - 1][n - 1])