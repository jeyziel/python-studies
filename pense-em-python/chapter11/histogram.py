
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('banana')
print(h)

##caso a chave exista no dicionário, o seu valor correspondete é retornado.
##; se nao for o caso, ele retorna o valor padrão.
print(h.get('a'))
print(h.get('a', 0))
print(h.get('a', 3))

print(h.get('b'))
print(h.get('c', 0))
