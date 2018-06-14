##a única diferença entre tupla que as lista é que elas são imutáveis
t = 'a','b','c','d','e'

s = (1,2,3,4,5,6,7)

print(t)

##para criar uma tupla com um único elemento, é necessário colocar uma virgula

a = 'a',

print(a, type(a))

##Um único valor entre parênteses sem a presença de virgula não é uma tupla
t2 = ('a')

print(t2, type(t2))

##como tuplas são imutáveis, você não pode alterar os elementos, mas pode substituit uma tupla por outra
t = ('A',) + s[2:]
print(t)
