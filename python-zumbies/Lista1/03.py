#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Informe a quantidade de dias \n'))
horas = int(input('Informe a quantidade de horas \n'))
minutos = int(input('Informe a quantidade de minutps \n'))
segundos = int(input('Informe a quantidade de segundos \n'))

diasParaSegundos = (dias * 24) * 60 * 60
horasParaSegundos = horas * 60 * 60
minutosParaSegundos = minutos * 60

totalSegundos = diasParaSegundos + horasParaSegundos + minutosParaSegundos + segundos

print('A quantidade de segundos eh: ', totalSegundos)




