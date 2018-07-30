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

def subtract(d1, d2):
    """ Return a dictionary with all keys that appear in d1 but not d2"""
    return set(d1) - set(d2)

hist = process_file('book.txt', True)
words = process_file('words.txt', False)

diff = subtract(hist, words)
print("The words in the book that aren't in the word list are: ")
for word in diff:
    print(word, end= ' ')
