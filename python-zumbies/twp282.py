'''
verificar se a palavra digitada é palindromo
'''
palavra = input('Informe uma palavra ')

if palavra == palavra[::-1]:
    print('é palindromo')
else:
    print('nao eh palindromo')

