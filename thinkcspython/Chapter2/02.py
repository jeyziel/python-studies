'''
Você olha para um relógio e são exatamente 2 da tarde. Você coloca um alarme para tocar daqui a 51 horas. A que horas o alarme ira tocar?
'''

hora_atual = 14

alarme_duracao = 51

alarme_tocar = (hora_atual + alarme_duracao) % 24

print('o alarme vai tocar ás {} horas'.format(alarme_tocar))