"""
calcule a média de 10 numeros inteiros
"""

cont = 0
soma = 0

while cont < 10:
    x = int(input('Informe o numero'))
    soma = soma + x
    cont = cont + 1

print('A média dos numeros eh : %.2f ' %(soma / cont))