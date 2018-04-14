"""
Verifique se um inteiro positivo n é primo.
"""

num = int(input('iNFORME O NUMERO '))
i = 1
cont = 0

while i <= num:
    if num % i == 0:
        cont = cont + 1
    i += 1
if cont == 2:
    print('o numero eh primo')
else:
    print('o Numero não eh primo')