

def _count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count

print(_count('banana', 'n'))