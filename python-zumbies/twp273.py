i = 0
notas = []
soma = 0

while i < 4:
    nota = float(input('Informe sua nota'))
    notas.append(nota)
    soma += nota
    i += 1
print('A soma das notas eh (%d) e a média %.2f ' %(soma, soma / i))