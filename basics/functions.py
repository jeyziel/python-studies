def call_numbers():
    for number in range(1,11):
        print(number)

def call_numbers_with_limiters(limit):
    list = range(0,10)
    for number in list[0:limit]:
        print (number)

def calculator(x, y):
    return x + y 


def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end='')
           


call_numbers()

print ("limit 5")

call_numbers_with_limiters(5)   

print("A soma de 5 + 10 eh:", calculator(5,10))

print("A soma de 2 + 3 eh", calculator(y = 2, x = 3))