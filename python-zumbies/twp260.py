"""
calculadora de 1 a 100
"""

x = 1

while x <= 10:
    n = 1
    print('tabuada do numeros %d \n' %x)
    while n <= 10:
        print ('%d x %d = %d ' %( x, n, x * n ))
        n = n + 1
    x = x + 1