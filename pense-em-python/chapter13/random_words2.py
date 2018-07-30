import string
import random
import time
from bisect import bisect_left

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
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def random_word(h):
    freqs = []
    words = list(h.keys())
    total_freq = 0

    for word, freq in h.items():
        total_freq += freq
        freqs.append(total_freq)

    x = random.randint(0, total_freq - 1)
    index = bisect_left(freqs, x)
    print(index)
    return words[index]

old_time = time.time()
hist = process_file('book.txt', True)
print(random_word(hist))

print(time.time() - old_time)
