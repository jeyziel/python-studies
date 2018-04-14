"""
Faça um Programa que peça os três lados de um triângulo.
O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo,
 se o mesmo é: equilátero, isósceles ou escaleno.
"""

a = int(input('Informe o valor do lado a'))
b = int(input('Informe o valor do lado b'))
c = int(input('Informe o valor do lado c'))

if a + b > c or a + c > b or b + c > a:
    print('é um triângulo \n')

    if a == b and b == c:
        print('triângulo equilátero')
    elif a == b or b == c or c == a:
        print ('triângulo isosceles')
    else:
        print('triângulo escaleno')
else:
    print ('não eh um triângulo')
