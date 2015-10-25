"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    if str(n) == str(n)[::-1]: return True
    return False

largest = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        product = a*b
        if is_palindrome(product):
            if product > largest: largest = product

print(largest)


"""
def create_palindromes:
    min = 10 * 10
    max = 99 * 99

    #get lengt of max
    #get half numbe rof length rounded up
    #make palindromes
"""