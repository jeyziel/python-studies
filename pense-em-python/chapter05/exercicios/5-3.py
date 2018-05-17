'''
verificar se é um triângulo
'''

a = int(input('Informe o valor de A'))
b = int(input('Informe o valor de B'))
c = int(input('Informe o valor de C'))

def is_triangule(a, b, c):
    if a < b + c or b < a + c or c < a + b:
        return True
    return False

is_triangule(a,b,c)