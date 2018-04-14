# coding=utf-8
while True:
    n = int(input('Informe uma nota entre 0 e 10 '))

    #if 0 <= n <= 10:
    if n >= 0 and n <=10:
        break
    else:
        print('Valor inválido, informe um novo valor ')

