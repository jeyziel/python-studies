#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Informe a quantidade dem km'))
dias = float(input('Informe a quantidade de dias'))

preco = (60.00 * dias) + (0.15 * km)

print('o preco eh de: ', preco)