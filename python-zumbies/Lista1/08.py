##Converta uma temperatura digitada em fahrenheit para celsius. 
# F = 9*C/5 + 32

fahrenheit = float(input('Informe a temperatura em fahrenheit'))

fahrenheit_to_celsius = (fahrenheit - 32) / (9/5)

print('A temperatura de %.2f em celsius eh : %.2f' %(fahrenheit, fahrenheit_to_celsius))
