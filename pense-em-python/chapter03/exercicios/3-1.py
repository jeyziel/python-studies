'''
Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:
'''

def right_justify(s):
     print (' '*(70-len(s))+s)

# def right_justify(s):
#     lenght = 70 - len(s)

#     justify = ''
#     for i in range(lenght):
#         justify += ' '
    
#     justify += s
#     print(justify)


right_justify('jeyziel')