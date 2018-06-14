
##atribuição de tupla

##trocar valors de a e b

a = 5
b = 10
a,b = b, a

print(a, b)

##exemplo com fibonnaci

def fib(n):
    a, b = 0, 1
    while a < n:
       print(a, end=' ')
       a, b = b, a+b
    print()
fib(5)


def fib2(n):
    cont = 1
    a = 0
    b = 1
    while cont < n - 1:
        a,b = b, a + b
        cont += 1
    return b

print(fib2(5))

def fib3(n):
    i = 0
    a = 0
    b = 1
    while i < n - 2:
        a,b = b, a + b
        i +=1
    return b

print(fib3(7))
