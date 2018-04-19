##função fatorial

def fatorial(x):
    i = 1
    fat = 1
    while x > 1:
        fat = fat * x
        x = x - 1
    return fat

for i in range(6): print(fatorial(i))

##variavel local e global

a = 10

def muda_e_imprime():
    a = 5 ## caso queira torna esse novo valor global, deve-se usar 
    ##a palavra chave global
    print('a dentro da função %d' %a)
print('a antes de mudar %d' %a)
muda_e_imprime()
print('a depois de mudar %d' %a)

