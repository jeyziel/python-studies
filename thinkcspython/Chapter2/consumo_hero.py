'''
Escreva um programa que calcula o consumo de gasolina de uma carro em quilômetros por litro. O programa deve pedir ao usuário que entre com o número de quilômetros percorridos e o número de litros de gasolina consumidos. Em seguida o programa deve imprimir a resposta.
'''

km_percorridos = int(input('Informe a quantidade de quilômetros'))
litros_gasolina = int(input('Informe a quantidade de gasolina consumidade'))

consumo_gasolina_litro = litros_gasolina / km_percorridos

print('O consumo de gasolina foi de {} litro(s) por KM'.format(consumo_gasolina_litro))

