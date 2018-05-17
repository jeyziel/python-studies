'''
Um número a é uma potência de b se for divisível por b e a/b for uma potência de b. Escreva uma função chamada is_power que receba os parâmetros a e b e retorne True se a for uma potência de b. Dica: pense no caso-base.
'''

def is_power(a, b):
    if a == 1:
        return True
    if a % b != 0 or a < b:
        return False
    return is_power(a/b, b)

print(is_power(27, 3))
print(is_power(1, 2))
print(is_power(6, 2))
print(is_power(0, 4))
print(is_power(4, 4))