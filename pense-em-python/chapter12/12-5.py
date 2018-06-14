#zip é uma função integrada que recebe duas ou mais sequências e devolve uma lista de tuplas onde cada tupla contém um elemento de cada sequência.

s = ['a', 'b', 'c']
t = [1,2,3,4,5]

for pair in zip(s, t):
    print(pair)

b = list(zip(s, t))
print(b)

print(b[0][0])
