# returns the total number of digits numbers with the specified number of digits
def positions(digits):
    return digits * 9 * 10 ** (digits - 1)

# Returns which number (index) the nth digit is in
def nth(index):
    digits = 0
    while True:
        digits += 1
        if index > positions(digits):
            index -= positions(digits)
        else: return index, digits

# returns the number of the index
def nth_digit(input):
    input = nth(input)
    if input[1] == 1: return input[0]
    number = 10 ** (input[1] - 1) + input[0] // input[1]
    return str(number)[(input[0] % input[1]) - 1]

solution = 1
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    solution *= int(nth_digit(i))
print(solution)
