# coding=utf-8
'''
Pergunte a velocidade de um carro, supondo
um valor inteiro. Caso ultrapasse 110 km/h,
exiba uma mensagem dizendo que o usuário
foi multado. Neste caso, exiba o valor da
multa, cobrando R$ 5,00 por km acima de
110.
'''

velocidade = int(input('Informe a velocidade do carro em km/h : '))

if velocidade > 110:
    print('Você foi multado em  R$ ', (velocidade - 110) * 5.00)
