import random

lista = []

while len(lista) < 15:
    numero = random.randint(10, 100)
    if numero not in lista:
        lista.append(numero)
lista.sort()
print(lista)