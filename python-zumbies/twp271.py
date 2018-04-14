##ler um vetor de 5 posições e mostrar

i = 0
vetor = []

while i < 5:
    num = int(input('Informe o %d valor' %(i+1)))
    vetor.append(num)
    i = i + 1
print(vetor)