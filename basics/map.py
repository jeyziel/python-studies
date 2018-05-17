import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(math.factorial, numbers))

print(squared_numbers)