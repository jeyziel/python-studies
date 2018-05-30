'''
Esta pergunta é baseada em um quebra-cabeça veiculado em um programa de rádio chamado Car Talk (http://www.cartalk.com/content/puzzlers):

Dê uma palavra com três letras duplas consecutivas. Vou dar exemplos de palavras que quase cumprem a condição, mas não chegam lá. Por exemplo, a palavra committee, c-o-m-m-i-t-t-e-e. Seria perfeita se não fosse aquele ‘i’ que se meteu ali no meio. Ou Mississippi: M-i-s-s-i-s-s-i-p-p-i. Se pudesse tirar aqueles ‘is’, daria certo. Mas há uma palavra que tem três pares consecutivos de letras e, que eu saiba, pode ser a única palavra que existe. É claro que provavelmente haja mais umas 500, mas só consigo pensar nessa. Qual é a palavra?

Escreva um programa que a encontre.

Solução: http://thinkpython2.com/code/cartalk1.py.
'''

def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count +=1
            if count == 3:
                return True 
            i = i + 2
        else:
            count = 0
            i += 1
    return False

with open('../words.txt') as _file:
    for line in _file:
        word = line.strip()
        if is_triple_double(line):
            print(line)

print(is_triple_double('aabbccd'))
print(is_triple_double('abbccdd'))
print(is_triple_double('aarara'))