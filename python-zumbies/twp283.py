##trocar vogais por *

texto = input('Informe a palavra : ')
new_palavra = ''
i = 0

while i < len(texto):
    if texto[i] not in 'aeiou':
        new_palavra += texto[i]
    else:
        new_palavra += '*'
    i = i + 1
print(new_palavra)