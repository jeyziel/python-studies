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

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

hist = process_file('book.txt', True)
print('Total number of words ', total_words(hist))
print('Number of different words ', different_words(hist))
