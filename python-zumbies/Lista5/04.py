'''
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?

Resposta: 7995
'''

start = 18644
end = 33087
cont = 0

while start <= end:
    if '2' in str(start):
        if '7' not in str(start):
            cont = cont + 1
    start += 1
    
print(cont)

