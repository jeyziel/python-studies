'''
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.
'''
import random

list1 = []
list2 = []
list3 = []

for i in range(10):
    list1.append(random.randint(1, 100))
    list2.append(random.randint(1, 100))

    list3.append(list1[i])
    list3.append(list2[i])

print(list1)
print(list2)
print(list3)