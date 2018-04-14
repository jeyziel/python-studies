'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
'''

valor_conta = float(input('Informe o valor da conta '))
valor_pagamento = float(input('Informe o valor do pagamento'))

notas = [50, 20, 10, 5, 2, 1]

troco =  valor_pagamento - valor_conta
i = 0

while troco > 0:
    qnt_notas = troco / notas[i]
    troco = troco % notas[i]

    if qnt_notas != 0:
        print("%d nota(s) de %d reai(s)" %(qnt_notas, notas[i]))
    i = i + 1