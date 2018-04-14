#Converta uma temperatura digitada em Celsius para Fahrenheit. 
# F = 9*C/5 + 32

celsius = float(input('Informe a temperatura em celsius \n'))

celsius_to_fahrenheit = 9 * (celsius / 5) + 32

print('A temperatura %f em fahreinheit eh : %f' %(celsius, celsius_to_fahrenheit))