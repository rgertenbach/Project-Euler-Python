"""

"""
"""
def coll(n):
    if n % 2 == 0: return int(n / 2)
    return int(n * 3 + 1)

c = {
    1: 0
}

for n in range(1,1000000):
    number = int(n)
    temp_dictionary = {}
    while number not in list(c.keys()):
        temp_dictionary[number] = 0
        number = coll(number)

        for i in temp_dictionary.keys():
            temp_dictionary[i] += 1
    for i in temp_dictionary.keys():
        temp_dictionary[i] += c[number]
        c[i] = temp_dictionary[i]
print(max(c.values()))
"""
"""
limit = 100
numberlimit = limit ** 100
numbers = []
current_numbers = [1]
carryover_numbers = []
steps = 1
while len(numbers) < limit - 1:
    steps += 1
    carryover_numbers = []
    #print(current_numbers)
    for number in current_numbers:
        if number < limit: numbers.append(number)
        if number < numberlimit: carryover_numbers.append(number*2)
        if (number - 1) % 3 == 0 and (number - 1) / 3 % 2 == 1 and number != 1 and number != 4: carryover_numbers.append((number - 1) / 3)
    current_numbers = carryover_numbers
else: print(numbers[-1])
"""

largest = 1
longeststeps = 0

for number in range(2,1000000):
    n = number
    steps = 0
    while n != 1:
        if n % 2 == 0: n /= 2
        else: n = n * 3 + 1
        steps += 1

    if steps > longeststeps:
        largest = number
        longeststeps = steps

print(largest)
