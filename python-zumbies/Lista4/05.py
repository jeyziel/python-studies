'''
Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais.

'''
text = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

def limpa_texto(text):
    texto = text.replace('.','')
    texto = text.replace(',','')
    texto = text.replace(':','').lower().split(' ')
    return texto

def verificar(p):
    for l in 'python':
        if l in p and len(p) > 4:
            return True
    return False 

new_texto = limpa_texto(text)
python_list = []

for palavra in new_texto:
    if verificar(palavra):
        python_list.append(palavra)

print("\n\nA quantidade de palavras que contém uma das letras de python e mais de 4 caracteres e: ", len(python_list))
print("\n\nLista com palavras que tem uma das letras de python e mais de 4 caracteres: ", python_list)
