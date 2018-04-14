i = 0
alfabeto = []
consoante = 0

while i < 10:
    caractere = input('Informe um caractere do alfabeto ')
    alfabeto.append(caractere)

    ##if alfabeto[i] not in 'aeiou'
    if not caractere in ('a','e','i', 'o','u'):
        consoante += 1
    i += 1
print('Foram lidos %d consoantes ' %consoante)