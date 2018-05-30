

def is_abecedarian(word):
    i = 0
    word = word.lower()
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True


print(is_abecedarian('Kaeikou'))   