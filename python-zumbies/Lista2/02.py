"""
Determine se um ano é bissexto.
"""

ano = int(input('Informe o ano'))


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano %d eh bissexto ' %ano)
else:
    print('o ano %d nao eh bissexto ' %ano)