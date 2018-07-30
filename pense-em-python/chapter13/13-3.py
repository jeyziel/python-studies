import string

def process_file(file, skip_header = False):
    hist = {}
    with open(file) as fp:
        if skip_header:
            skip_header_book(fp)

        for line in fp:
            process_line(line, hist)

    return hist

def skip_header_book(fp):
    for line in fp:
        if line.startswith('THE BOOK OF FRIENDSHIP'):
            break

def process_line(line, hist):
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        word = word.strip(strippables)
        word = word.lower()

        ##update the histogram
        hist[word] = hist.get(word, 0) + 1

def most_common(hist):
    t = []
    for key,value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t

hist = process_file('book.txt', True)
print('The 10 most common words ', most_common(hist)[:20])
