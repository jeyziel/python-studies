###modulo random
import random

times = ['bahia','vitoria', 'vasco', 'palmeiras']

print(random.randint(1, 100))

print(random.choice(times))

random.shuffle(times) ##embaralha a lista de times


def embaralha(words):
    lista = list(words)
    random.shuffle(lista)
    return ''.join(lista)



embaralhada = embaralha('mamae mandou')

print(embaralhada)    