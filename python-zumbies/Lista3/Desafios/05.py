'''
Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
'''
from typing import Any, Union

num = int(input('Informe um numero '))

invertido = []
i = 0
string = ''

while num > 0:
    cifra = num % 10
    string = string + str(cifra)
    invertido.append(cifra)
    num = num // 10


print(invertido, string)