#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Informe a distancia a ser percorrida'))
velocidade_media = float(input('Informe a velocidade média em km/h'))

print('O tempo de viagem é de : %.2f' %(velocidade_media/distancia))