from random import randint

secreto = randint(1,100)

while True:
    numero = int(input('Informe um numero '))

    if numero == secreto:
        print('você acertou ')
        break
    elif numero > secreto:
        print('voce chutou alto')
    else:
        print('vc chutou baixo ')     