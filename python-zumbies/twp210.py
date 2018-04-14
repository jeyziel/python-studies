"""
digite os numeros pares entre 0 e o um número determinado pelo usuario

"""

n = int(input('Informe um numero'))
cont = 0

while n >= cont:
    if cont % 2 == 0:
        print('o %d eh par ' %cont )
    cont = cont + 1
