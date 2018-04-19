'''
passar para python
para i = 1 até 9
se i != 3, então
para j = 1 até 6
imprime 'oi'

Resposta: 48

'''

cont = 0
for i in range(9):
    if i != 3:
        for j in range(6):
            print('oi')
            cont += 1

print(cont)