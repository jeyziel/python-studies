'''
O matemático Srinivasa Ramanujan encontrou uma série infinita que pode ser usada para gerar uma aproximação numérica de 1/π:

Fórmula – Aproximação de π pela série de Ramanujan.

Escreva uma função chamada estimate_pi que use esta fórmula para computar e devolver uma estimativa de π. Você deve usar o loop while para calcular os termos da adição até que o último termo seja menor que 1e-15 (que é a notação do Python para 10 ** 15). Você pode verificar o resultado comparando-o com math.pi.

'''
import math
from decimal import Decimal

def estimative_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = math.factorial(4*k) * (1103 + 26390*k)
        denom = (math.factorial(k) ** 4) * (396 ** (4*k))
        term = float(factor * num / denom)
        total += term

        if abs(term) < 1e-15 : break 
        k += 1
    return 1 / total

print(estimative_pi())


