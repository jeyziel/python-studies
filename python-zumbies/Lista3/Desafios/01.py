##numero triangular

i = 1
num = int(input('Informe o numero e verifique se ele é triangular '))
triangular = False

while i * (i+1) * (i+2) <= num:
    if i * (i+1) * (i+2) == num:
        triangular = True
    i = i + 1

print('%d é triangular? ' %(num), triangular)