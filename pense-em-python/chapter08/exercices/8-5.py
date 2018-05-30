
# print(ord('e') - ord(chr(10)))

# print(chr(59))


def rotate_word(word, num):
    text = ''
    for i in word:
        rotate = ord(i) + num
        text += chr(rotate)
    return text

print(rotate_word('melon', -10))

