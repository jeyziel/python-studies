'''
O unpacking é o processo que é executado dentro da função, e não na
chamada. Podemos usar a sintaxe *args ou **kwargs como argumentos
para o unpacking dos parâmetros posicionais ou nomeados.

'''

def unpacking_arguments(*args):
    print(args)
    print(args[0])
    print(args[1:])

##recebe um numero arbitrário de parâmetros 
unpacking_arguments(1, 2 , 3 ,4 ,5)

'''
O mesmo aplica-se aos parâmetros nomeados. Se usarmos **kwargs , o
chamador pode passar quaisquer parâmetros nomeados que podem acessar
kwargs como um dicionário e obter os valores.
'''

def unpacking_experiment(**kwargs):
    print(kwargs)

unpacking_experiment(named = "teste", other = "other")