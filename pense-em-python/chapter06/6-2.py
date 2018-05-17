'''
Distância entre dois pontos
Usar o teorema de pitágoras
'''
import math

def distance(x1, y1, x2, y2):
    dx = x1 - y2
    dy = x2 - y2
    dsquared = dx ** 2 + dy ** 2
    return math.sqrt(dsquared)

print(distance(1, 2, 4, 6))