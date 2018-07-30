import string

def process_file(filename):
    new_line = []
    with open(filename) as fn:
        for line in fn.readlines():
            new_line.append(process_line(line))
    return '\n'.join(new_line)

def process_line(line):
    new_word = []
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace
    for word in line.split():
        word = word.strip(strippables)
        word = word.lower()
        if word:
            new_word.append(word)
    return ' '.join(new_word)

print(process_file('jeyziel.txt'))

# print(process_line('Está*** chovendo em São Paulo e curaçá '))
