'''
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.
'''
import random

lista = []
menor = 1
maior = 1
for i in range(10):
    lista.append(random.randint(1, 100))

for i in range(10):
    if lista[menor] > lista[i]:
        menor = i

    if lista[maior] < lista[i]:
        maior = i

print(lista)
print('O maior numero eh : %d e o menor : %d' %(lista[maior], lista[menor]))            