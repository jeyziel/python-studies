
def most_frequent(s):

    hist = make_histogram(s)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    return res

def make_histogram(s):
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

def read_file(filename):
    return open(filename, 'r').read()

if __name__ == '__main__' :
    words = read_file('words.txt').replace('\n', '')
    freq_words = most_frequent(words)
    print(freq_words)
