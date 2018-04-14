'''
Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator
'''

num = int(input('Informe o numero '))
fator = 2  # type: int
fatores = []

while num > 1:
    if num % fator == 0:
        num = num / fator
        fatores.append(fator)
    else:
        fator += 1

print('fatores primos ', fatores)