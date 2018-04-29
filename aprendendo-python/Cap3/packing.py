from datetime import date

d = (2018, 5, 29)

print(date(d[0], d[1], d[2]))

'''
se os valores que estão nas tuplas/lista
estiverem na ordem dos parâmetros que a função recebe
podemos usar o packing
'''

print(date(*d))

'''
O que aconteceu aqui é que se date espera os parâmetros year , month ,
day e temos uma lista ou tupla com os valores que casam essa ordem, po demos usar a sintaxe do *tupla para sinalizar que a coleção deve ter suas posições casadas com parâmetros recebidos.
'''


'''
O packing também vale para os parâmetros nomeados.
Neste caso a sintaxe é o **dicionário, o interpretador python automaticamente casa os valores do dicionario com os parametros nomeados da função
'''
def new_user(active = False, admin = True):
    print(active)
    print(admin)

config = {"active" : True, "admin" : False}

new_user(**config)