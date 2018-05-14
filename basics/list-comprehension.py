##double prize
prizes = [50, 40, 90, 80, 100]

double_prizes = []
for prize in prizes:
    double_prizes.append(prize * 2)

print(double_prizes)

##comprehension method

double_prizes = [ prize * 2 for prize in prizes ] 

print(double_prizes)

##squared even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

squared_even_numbers = [num ** 2 for num in numbers if (num ** 2) % 2 == 0 ]

print(squared_even_numbers)