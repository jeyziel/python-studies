'''
Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se
'''
text = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

def limpa_texto(text):
    texto = text.replace('.','')
    texto = text.replace(',','')
    texto = text.replace(':','').lower().split(' ')
    return texto

def verificar(p):
    for l in 'python':
        if p.startswith(l) or p.endswith(l):
            return True
    return False 

new_texto = limpa_texto(text)
python_list = []

for palavra in new_texto:
    if verificar(palavra):
        python_list.append(palavra)

print("Lista original: \n", new_texto)
print("\n\nLista com iniciadas ou terminadas com uma das letras de python: \n", python_list)