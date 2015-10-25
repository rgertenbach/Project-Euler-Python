"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import time

def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

start_time = time.time()

perm = 10**5000-1
digits = [i for i in range (1776)]
result = []

while perm > 0 :
    f=fact(len(digits) - 1)
    position = perm // f
    perm -= f * position
    result.append(digits.pop(position))

for x in digits:
    result.append(x)

print("--- %s seconds ---" % (time.time() - start_time))
print("".join(str(x) for x in result))