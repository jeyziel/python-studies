##tuplas como argumentos variáveis

#printall recebe qualquer número de argumento e os exibe:

def printall(*args):
    print(args)

printall(1 ,23, 4)

## o complemento de de reunir é espalhar. Se você tiver uma sequência de valores e quiser passá-la a uma função como argumentos múltiplos, pode usar o operador *.
t = (15, 4)

print(divmod(*t))
