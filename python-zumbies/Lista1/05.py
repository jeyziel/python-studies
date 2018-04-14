#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input('Informe o preco da mercadoria \n'))
desconto = float(input('Informe o desconto \n'))

valorDesconto = preco * (desconto/100)
precoTotal = preco - valorDesconto

print('Valor do desconto %.2f e o valor do preco a pagar eh : %.2f \n' %(valorDesconto, precoTotal))