

def is_reverse(word1, word2):
    if len(word1) != len(word2) : return False
    i = len(word1) - 1
    j = 0

    while i >= 0:
        print(i, j)
        if word1[i] != word2[j] : return False
        i = i - 1
        j = j + 1
    
    return True


print(is_reverse('pots', 'stop'))