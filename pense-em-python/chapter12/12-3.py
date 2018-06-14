##tuplas como valores de retorno
t = divmod(7, 3)

print(t)

##guardar o quociente e o dividor remenescente
quot, rem = divmod(16, 3)
print(quot)
print(rem)

t = [5, 10, 90, 10, 80, 70, 110]
##exemplo de função que retorna uma tupla
def min_max(t):
    return min(t), max(t)

print(min_max(t))
