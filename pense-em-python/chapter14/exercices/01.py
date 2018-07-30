
def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()

sed('banana', 'tangerina', 'name.txt', 'name.txt.replace')
