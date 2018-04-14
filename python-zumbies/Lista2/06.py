salario_hora = float(input('Quanto você ganha por hora?'))
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas'))

salario_bruto = salario_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

impostos = imposto_renda + inss + sindicato

salario_liquido = salario_bruto - impostos

print('salario bruto %.2f' %salario_bruto)
print('imposto de renda %.2f' %imposto_renda)
print('inss %.2f ' %inss)
print('sindicato %.2f ' %sindicato)

print('salario liquido %.2f' %salario_liquido)