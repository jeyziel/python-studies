texto = open('mensagem.txt')
saida = open('cripto.txt', 'w')

for linha in texto.readlines(): ##lê cada linha do arquivo
    for letra in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)

texto.close()
saida.close()                