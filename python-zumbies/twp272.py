##ler 5 valores e mostrar na ordem inversa

vetor = []

i = 0

while i < 10:
    n = float(input('Informe o numero : '))
    vetor.append(n)
    i += 1

i = 9

while i >= 0:
    print(vetor[i])
    i -= 1