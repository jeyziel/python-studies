'''
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7?
Resposta: 183
'''

start = 1067
end = 3627
cont = 0

while start <= end:
    if start % 7 == 0 and start % 2 ==0:
        cont = cont + 1
    start += 1

print(cont)