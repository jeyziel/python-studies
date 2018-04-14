#calcular a media das nota

notas = [7, 8.5, 5 , 10, 3]

soma = 0
cont = 0

for nota in notas:
    soma = soma + nota
    cont += 1

print('A media das notas eh : %.2f ' %(soma/cont))