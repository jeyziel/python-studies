"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

n1 = int(input('Informe o primeiro numero'))
n2 = int(input('Informe o segundo numero'))
n3 = int(input('Informe o terceiro numero'))

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menor = n3
elif n2 > n1 and n2 > n3:
    maior = n2
    if n3 < n1:
        menor = n3
    else:
        menor = n1
else:
    if n1 < n2:
        menor = n1
    else:
        menor = n2

print('o MAIOR número eh %d e o menor %d' %(maior, menor))