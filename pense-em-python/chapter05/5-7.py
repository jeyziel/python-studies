x = 9

if x > 0 and x < 10:
    print('x is a positive single-digit number')

##podemos tbm fazer essa operação de uma forma mais concisa

if 0 < x < 10:
     print('x is a positive single-digit number')

lista = [1,1,1,1,2,2,2,2,4,4,6,6,9,9,9]

def teste(n):
    if n == 6:
        return 3
    elif n == 9:
        return 5
    else:
        return n

new_lista = sorted(list(map(teste, lista)))

print(new_lista)