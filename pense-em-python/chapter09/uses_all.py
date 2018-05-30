

def uses_all(word, available):
    for letter in available:
        if letter not in word:
            return False
    return True


print(uses_all('babebibobu', 'aeiouy'))