"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
"""

m2 = int(input('Informe o tamanho em m²'))

if m2 % 54 == 0:
    tintas = (m2 // 54)
else:
    tintas = (m2 // 54) + 1

preco = tintas * 80



print('serão necessario %d tintas para pintar %d metros e o preco eh de %d reais' %(tintas, m2, preco))
