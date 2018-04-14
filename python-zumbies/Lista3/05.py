##algoritmo de euclides

a = int(input('Informe o primeiro numero'))
b = int(input('Informe o segundo numero'))

while a % b != 0:
    aux = a % b
    a = b
    b = aux

#python form

while a % b != 0:
    a,b = b, a % b

print('MDC = %d' %b)