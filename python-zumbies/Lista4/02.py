'''
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.
'''
import random

lista = []
even = []
odd = []

for i in range(20):
    number = random.randint(1, 100)
    lista.append(number)

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(lista)

print('numeros pares', even)            
print('numeros ímpares', odd)            