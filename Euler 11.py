def maxx(x,y):
    return max(x,y)

f = open("E:\OneDrive\Python\Euler\Euler 11.txt", 'r')
grid = []
maxp = 0

for line in f:
    grid.append([int(x) for x in line.split()])

size = len(grid)

for row in range(size):
    for col in range(size):
        if row <= size - 4: maxp = maxx(grid[row][col] * grid[row+1][col] * grid[row+2][col] * grid[row+3][col], maxp)
        if col <= size - 4: maxp = maxx(grid[row][col] * grid[row][col+1] * grid[row][col+2] * grid[row][col+3], maxp)
        if row <= size - 4 and col <= size - 4: maxp = maxx(grid[row][col] * grid[row+1][col+1] * grid[row+2][col+2] * grid[row+3][col+1], maxp)
        if row >= 3 and col <= size - 4: maxp = maxx(grid[row][col] * grid[row-1][col+1] * grid[row-2][col+2] * grid[row-3][col+3], maxp)
f.close()
print(maxp)