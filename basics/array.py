
array = [1,2,3,4,5,6]
array2 = [7,8,9,10]

print(array + array2)

numbers = array + array2

print(numbers[0:3])

numbers.append(15)

print(numbers)

##
#deletar através do valor
#
print ("removendo o 1")
numbers.remove(1)

print(numbers)

##
#deletar através do indice
#remove 0 6
del(numbers[4])

print(numbers)
