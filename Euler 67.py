"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem, as there are 299 altogether!
If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
"""

file = []
with open("E:\OneDrive\Python\Euler\Euler 67.txt", "r") as f:
    for row in f:
        file.append(list(map(int, row.split())))

for row in range(len(file) - 2, -1, -1):
    for column in range(len(file[row])):
        if file[row + 1][column] > file[row + 1][column + 1]:
            file[row][column] += file[row + 1][column]
        else:
            file[row][column] += file[row + 1][column + 1]
print(file[0][0])