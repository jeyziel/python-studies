'''
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.
'''

qnt_cigarros_por_dia = int(input('Informe a quantidade de cigarros fumados por dia : '))
anos = int(input('A quantos anos você é fumante : '))

num_cigarros = qnt_cigarros_por_dia * anos * 365
dias_perdidos = (num_cigarros * 10) / (60 * 24)

print('Você já perdeu %d de vida' %dias_perdidos)