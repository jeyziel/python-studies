arquivo = open('arquivo.txt', 'r')

for linha in arquivo.readlines():
    print(linha.rstrip()) ##rstrip retira o \n do arquivo
arquivo.close()    