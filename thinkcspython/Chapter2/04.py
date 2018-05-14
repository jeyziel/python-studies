'''
It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.
'''

dia_mes = int(input('Informe o dia do mês '))
dia_semana = int(input('Informe o dia da semana de 0 a 6 '))

dias_ferias = int(input('Informe a quantidade de dias de férias'))

dia_semana_retorno = (dias_ferias % 7) + dia_semana

print('Eu irei voltar no dia {} da semana'.format(dia_semana_retorno))
