

_file = open('words.txt')

for line in _file:
    if len(line.strip()) > 20:
        print(line)