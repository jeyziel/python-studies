##solicitar a data no formato DD/MM/AAAA e imprimir com o nome do mês por extenso

meses = ['janeiro', 'fevereiro', 'março'
      'abril', 'maio','junho', 'julho',
       'agosto', 'setembro', 'outubro', 'novembro',
       'dezembro'
      ]

# data = input('Informe a sua data de nascimento no formato (DD/MM/AAAA)')
#
# data_split = data.split('/')
# dia = int(data_split[0])
# mes = int(data_split[1])
# ano = int(data_split[2])

# print(dia, mes, ano, meses[(int(mes) - 1)])

dia, mes, ano = input('Informe a sua data de nascimento no formato DD/MM/AAAA ').split('/')

print('%s de %s de %s' %(dia, meses[int(mes) - 1], ano))