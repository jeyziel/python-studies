import random

def dict_word():
    _file = open('../words.txt')
    d = {}
    for word in _file:
        word = word.strip()
        d[word] = random.randint(1, 100)
    return d

print(dict_word())
