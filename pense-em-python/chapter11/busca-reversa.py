'''
{'a' : 3, 'b' : 1, 'n': 2}
k = 'n'
v = d[k]
v = 2

fazer isso é tranquilo, certo?

Mas, e se você tiver V, e quiser encontrar k?

'''

def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError(f'value {v} does not appear in the dictionary')

h = histogram('banana')
print(h)

reverse = reverse_lookup(h, 2)
print(reverse)

reverse = reverse_lookup(h, 4)
