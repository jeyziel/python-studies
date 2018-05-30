

def has_no_e():
    _file = open('words.txt')
    count_line = 0
    has_e = 0
    for line in _file:
        if line.strip().count('e') <= 0:
            print(line.strip())
            has_e += 1
        count_line += 1
    
    print('A porcentagem de palavras que não tem "e" é de %.2f %' %((has_e / count_line)*100))

has_no_e()