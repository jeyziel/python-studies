##metodos de string

arquivo = 'prog.py'

print(arquivo.startswith('p'))

print(arquivo.endswith('py'))

print(arquivo.upper())

##find e replace

texto = 'um tigre, dois tigres, três tigres'

print(texto.find('tigre')) ##primeira ocorrência de tigre está no indice 3
print(texto.find('tigre', 4))

##replace = troca a ocorrencia de uma palavra por outra

print(texto.replace('tigre','gato'))

##split e join
##split separada, join agrupa

#split
s = 'batatinha quando nasce'

print(s.split(' '))

data = '21/01/1999'
print(data.split('/'))

##join
times = ['vasco','bahia', 'vitoria', 'sport','palmeiras','flamengo']

print('/'.join(times))
