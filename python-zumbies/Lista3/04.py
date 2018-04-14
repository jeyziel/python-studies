##A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

num = int(input('Informe um numero'))
a = 1
b = 1
i = 1

while i <= num - 2:
    fib = a + b
    a = b
    b = fib
    print(fib)
    num = num - 1

print(fib)


##python form

a,b = 1,1
num = 8

while i <= num - 2:
    a,b = b, a + b
    i = i + 1

print('Fib(%d) = %d' %(num, b))
