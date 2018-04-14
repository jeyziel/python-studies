#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Informe o valor do salário'))
porcentagem = float(input('Informe o valor da porcetagem em %'))

valorAumento = salario * (porcentagem / 100)
novoValor = salario + valorAumento

print('O valor do aumento eh %.2f e o novo salário é de : %.2f' %(valorAumento, novoValor))


